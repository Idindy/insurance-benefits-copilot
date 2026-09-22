# Insurance Benefits Copilot

Portfolio AI application for broker/member benefit navigation using **synthetic data only**.

## What it demonstrates
- Retrieval-augmented benefit Q&A with source citations
- Structured plan/benefit extraction
- Lightweight PII redaction and audit events
- FastAPI service with deterministic local retrieval
- LLM-ready adapter: plug an approved model into the retrieved context
- Tests and Docker packaging

This is an engineering portfolio project, not a HIPAA-certified production system and not insurance advice.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs`, then POST to `/ask`:
```json
{"question":"What is the specialist copay on the Gold plan?"}
```

## Architecture
`synthetic plan docs -> chunk/index -> retrieve -> grounded answer -> citations + audit event`

The local answerer intentionally uses extractive grounding so the demo runs without API keys. `app/llm.py` defines the seam for an external LLM.