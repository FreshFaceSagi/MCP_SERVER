from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tools import TOOLS

app = FastAPI()

class ToolCall(BaseModel):
    tool_name: str
    arguments: dict = {}

@app.get("/tools")
def list_tools():
    return {
        "tools": [
            {
                "name": name,
                "description": meta["description"],
                "schema": meta["schema"]
            }
            for name, meta in TOOLS.items()
        ]
    }

@app.post("/tool-call")
def call_tool(payload: ToolCall):
    if payload.tool_name not in TOOLS:
        raise HTTPException(404, "Tool not found")
    tool = TOOLS[payload.tool_name]
    try:
        result = tool["fn"](**payload.arguments)
        return {"tool_name": payload.tool_name, "result": result}
    except Exception as e:
        raise HTTPException(500, str(e))