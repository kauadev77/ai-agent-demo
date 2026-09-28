from collections import defaultdict


class SupportAgent:
    """Small deterministic agent used to demonstrate agent orchestration."""

    def __init__(self) -> None:
        self.memory: dict[str, list[str]] = defaultdict(list)

    def classify_intent(self, message: str) -> str:
        text = message.lower()
        if any(word in text for word in ("order", "pedido", "delivery", "entrega")):
            return "order_status"
        if any(word in text for word in ("human", "person", "humano", "atendente")):
            return "human_handoff"
        return "faq"

    def run_tool(self, intent: str, message: str) -> tuple[str | None, str]:
        if intent == "order_status":
            digits = "".join(char for char in message if char.isdigit())
            order_id = digits or "demo"
            return "order_status", f"Order {order_id} is in transit. This is fictional demo data."

        if intent == "human_handoff":
            return "human_handoff", "A human handoff would be created here. No external system is called."

        return "faq_search", "This demo can answer order-status questions and demonstrate human handoff."

    def respond(self, conversation_id: str, message: str) -> dict[str, str | None]:
        self.memory[conversation_id].append(message)
        intent = self.classify_intent(message)
        tool, response = self.run_tool(intent, message)
        return {
            "conversation_id": conversation_id,
            "intent": intent,
            "tool": tool,
            "response": response,
        }
