import requests
import json
from llm_client import GroqChat
from  config import LLM_BASE_URL, LLM_PROVIDER, LLM_MODEL, LLM_API_KEY

MCP_BASE = "http://localhost:8000"

LLM_CLIENT = GroqChat(model=LLM_MODEL, api_key=LLM_API_KEY)
def run_request(user_message: str):
    # 1. Get tools
    tools_resp = requests.get(f"{MCP_BASE}/tools")
    tools_resp.raise_for_status()
    tools = tools_resp.json()["tools"]
    
    # 2. Ask LLM what to do
    llm_resp = LLM_CLIENT.call_llm_with_tools(user_message, tools)

    #print(f"LLM response (first choice): {llm_resp.get('choices')[0]}")
   # choice = llm_resp.choices[0].message


    if "tool_calls" not in llm_resp:
        print("LLM responded directly:", llm_resp["content"])
        return

    tool_calls = llm_resp["tool_calls"]
    tool_results = []

    # # 3. Execute tools
    parsed = []
    for tc in tool_calls:
        print(f"Processing tool call: {tc}")
        # tc is a ChatCompletionMessageToolCall object
        name = tc.function.name
        args = json.loads(tc.function.arguments)
        print(f"Calling tool: {name} with args {args}")
        parsed.append({"name": name, "args": args})
        tool_resp = requests.post(
        f"{MCP_BASE}/tool-call",
            json={"tool_name": name, "arguments": args},)
        print(f"Tool response status: {tool_resp.status_code}, content: {tool_resp.text}")
        tool_resp.raise_for_status()
        result = tool_resp.json()
        print(f"Tool result: {result}")
        tool_results.append(result)
        #print(f"Tool result: {result}")
    #return tool_results

  
    # for tc in tool_calls:
    #     name = tc["function"]["name"]
    #     args = json.loads(tc["function"]["arguments"])
    #     print(f"Calling tool: {name} with args {args}")

    #     tool_resp = requests.post(
    #         f"{MCP_BASE}/tool-call",
    #         json={"tool_name": name, "arguments": args},
    #     )
    #     tool_resp.raise_for_status()
    #     result = tool_resp.json()
    #     tool_results.append(result)

    # # 4. Final answer
    # final_resp = LLM_CLIENT.call_llm_with_tools(user_message, tools, tool_results=tool_results)
    # print(f"Final LLM response: {final_resp}")
    # final_msg = final_resp["choices"][0]["message"]["content"]
    # print("Final answer:\n", final_msg)
    print("tool_results tool calls:", tool_results)

if __name__ == "__main__":
    print(run_request("Get all commits from the main branch of the my-repo repository."))