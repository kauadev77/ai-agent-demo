from app.agent import SupportAgent


def test_classifies_order_intent() -> None:
    agent = SupportAgent()
    assert agent.classify_intent("Where is order 123?") == "order_status"


def test_order_tool_returns_fictional_status() -> None:
    agent = SupportAgent()
    result = agent.respond("test", "Where is order 123?")
    assert result["tool"] == "order_status"
    assert "123" in result["response"]


def test_memory_is_scoped_by_conversation() -> None:
    agent = SupportAgent()
    agent.respond("a", "hello")
    agent.respond("b", "hello")
    assert len(agent.memory["a"]) == 1
    assert len(agent.memory["b"]) == 1
