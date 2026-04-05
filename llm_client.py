import json
import re
from typing import Any
from groq import Groq
from config import LLM_API_KEY, LLM_MODEL


def _strip_json_fence(text: str) -> str:
    text = text.strip()
    m = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return text


class GroqChat:
    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        key = (api_key or LLM_API_KEY).strip()
        if not key:
            raise ValueError(
                "Missing GROQ_API_KEY. Create a free key at https://console.groq.com/keys "
                "and set it in .env or the environment."
            )
        self._client = Groq(api_key=key)
        self._model = model or LLM_MODEL

    #
    # ---------------------------------------------------------
    # Basic completion
    # ---------------------------------------------------------
    #
    def complete(
        self,
        system: str,
        user: str,
        *,
        temperature: float = 0.4,
        max_tokens: int = 4096,
    ) -> str:
        print(f"Calling LLM with system: {system} and user: {user}")
        resp = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        print(f"Response: {resp}")
        return (resp.choices[0].message.content or "").strip()

    def complete_json(
        self,
        system: str,
        user: str,
        *,
        temperature: float = 0.2,
        max_tokens: int = 4096,
    ) -> Any:
        raw = self.complete(system, user, temperature=temperature, max_tokens=max_tokens)
        cleaned = _strip_json_fence(raw)
        return json.loads(cleaned)

    #
    # ---------------------------------------------------------
    # Tool-enabled LLM call (FIXED)
    # ---------------------------------------------------------
    #
    def call_llm_with_tools(
        self,
        user_message: str,
        tools_spec: list,
        tool_results: list = None,
    ):
        messages = [
            {"role": "system", "content": "You are an assistant that can call tools."},
            {"role": "user", "content": user_message},
        ]

        if tool_results:
            messages.append({
                "role": "system",
                "content": f"Tool results: {json.dumps(tool_results)}",
            })

        # Convert MCP tool spec → Groq tool schema
        groq_tools = [
            {
                "type": "function",
                "function": {
                    "name": t["name"],
                    "description": t["description"],
                    "parameters": t["schema"],
                },
            }
            for t in tools_spec
        ]
        print(f"Calling LLM with tools: {groq_tools} and messages: {messages}")
        # Call Groq with tools enabled
        resp = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            tools=groq_tools,
            tool_choice="auto",
            temperature=0.0,
            max_tokens=5000,
        )
        print(f"LLM response: {resp}")
        msg = resp.choices[0].message

        #
        # If the LLM selected a tool, return the tool call
        #
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            return {
                "type": "tool_call",
                "tool_calls": msg.tool_calls,
            }

        #
        # Otherwise return normal text
        #
        return {
            "type": "message",
            "content": msg.content.strip() if msg.content else "",
        }