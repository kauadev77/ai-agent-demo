# AI Agent Demo

A small, production-minded **AI agent backend** built with FastAPI.

The project demonstrates an agent architecture with intent classification, tool selection, short-term conversation memory, API validation and tests. It runs locally without paid services and can later be connected to an LLM provider.

## Highlights

- FastAPI REST API
- Agent/service separation
- Intent classification
- Tool routing
- In-memory conversation context
- Pydantic request/response models
- Health endpoint
- Automated tests
- Docker support
- No company code, client data or private integrations

## Architecture

```text
Client
  |
  v
FastAPI
  |
  v
SupportAgent
  |---- intent classifier
  |---- conversation memory
  |---- tool router
  |
  +---- order_status
  +---- faq_search
  +---- human_handoff
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: `http://localhost:8000/docs`

## Example

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"conversation_id":"demo-1","message":"Where is order 123?"}'
```

## Tests

```bash
pytest
```

## Next steps

- Plug in an LLM provider through the agent interface
- Persist memory in PostgreSQL
- Add retrieval over a vector store
- Add authentication, observability and rate limiting
