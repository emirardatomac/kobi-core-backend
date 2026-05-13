from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.gemini_client import ask_gemini

from app.ai.prompts import (
    SYSTEM_PROMPT,
    FINAL_RESPONSE_PROMPT
)

from app.ai.parser import parse_ai_json

from app.ai.executor import (
    execute_tool
)


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    intent_prompt = f"""
    {SYSTEM_PROMPT}

    User:

    {request.message}
    """

    ai_decision = ask_gemini(
        intent_prompt
    )


    parsed = parse_ai_json(
        ai_decision
    )


    tool_result = execute_tool(
        parsed
    )


    final_prompt = f"""
    {FINAL_RESPONSE_PROMPT}

    {tool_result}
    """


    final_response = ask_gemini(
        final_prompt
    )


    return {
        "decision": parsed,
        "tool_result": tool_result,
        "response": final_response
    }