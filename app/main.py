from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel, Field
from .retrieval import PlanIndex
from .security import redact_pii
from .llm import grounded_answer

app = FastAPI(title="Insurance Benefits Copilot", version="0.1.0")
index = PlanIndex()
AUDIT_LOG = []

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/ask")
def ask(req: AskRequest):
    safe_question = redact_pii(req.question)
    hits = index.search(safe_question)
    answer = grounded_answer(safe_question, hits)
    event = {"at": datetime.now(timezone.utc).isoformat(), "action": "benefits_query", "pii_redacted": safe_question != req.question}
    AUDIT_LOG.append(event)
    return {"answer": answer, "citations": [{"source": h["source"], "score": round(h["score"], 3)} for h in hits], "audit": event, "disclaimer": "Synthetic demo; not insurance advice."}
