from fastapi import FastAPI

from app.agent import SupportAgent
from app.models import ChatRequest, ChatResponse


app = FastAPI(
    title="AI Agent Demo",
    version="1.0.0",
    description="Portfolio-safe AI agent architecture demo.",
)
agent = SupportAgent()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    result = agent.respond(payload.conversation_id, payload.message)
    return ChatResponse(**result)
