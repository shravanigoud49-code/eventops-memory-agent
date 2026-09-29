import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from memory.hindsight_memory import HindsightMemory

app = FastAPI(
    title="EventOps Memory Agent",
    description="Event operations intelligence powered by Hindsight long-term memory.",
    version="2.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

memory = HindsightMemory()

class EventRequest(BaseModel):
    event_type: str = Field(min_length=1)
    attendance: int = Field(gt=0)
    vendor: str = ""
    location: str = ""
    event_time: str = ""
    description: str = ""
    @field_validator("event_type", "vendor", "location", "event_time", "description", mode="before")
    @classmethod
    def clean_text(cls, value):
        return "" if value is None else str(value).strip()

class OutcomeRequest(BaseModel):
    event_id: str = Field(min_length=1)
    outcome: str = Field(min_length=1)
    actual_problem: str = Field(min_length=1)
    action_taken: str = Field(min_length=1)
    lesson_learned: str = Field(min_length=1)
    @field_validator("event_id", "outcome", "actual_problem", "action_taken", "lesson_learned", mode="before")
    @classmethod
    def clean_required_text(cls, value):
        if value is None or not str(value).strip():
            raise ValueError("This field is required.")
        return str(value).strip()

class RecallRequest(BaseModel):
    query: str = Field(min_length=1)

@app.get("/")
def home():
    return {"status":"online", "agent":"EventOps Memory Agent", "version":"2.0", "memory_source":"hindsight"}

@app.get("/api/health")
async def health():
    try:
        version = await memory.version()
        return {"status":"healthy", "service":"EventOps Backend", "memory_source":"hindsight", "hindsight_api_version":version}
    except Exception as exc:
        return {"status":"degraded", "service":"EventOps Backend", "memory_source":"hindsight", "error":str(exc)}

@app.post("/api/outcome")
async def record_outcome(outcome: OutcomeRequest):
    content = json.dumps({
        "event_id": outcome.event_id,
        "problem": outcome.actual_problem,
        "action": outcome.action_taken,
        "outcome": outcome.outcome,
        "lesson": outcome.lesson_learned,
        "domain": "eventops"
    }, ensure_ascii=False)
    try:
        result = await memory.retain_event(content)
        return {
            "status":"learned",
            "memory_source":"hindsight",
            "message":"Event outcome successfully retained in Hindsight.",
            "hindsight_result": serialize_result(result),
            "memory": {
                "event_id": outcome.event_id,
                "problem": outcome.actual_problem,
                "action": outcome.action_taken,
                "outcome": outcome.outcome,
                "lesson": outcome.lesson_learned,
                "tags":["eventops","hindsight","outcome","learned-lesson"]
            }
        }
    except Exception as exc:
        error_text = str(exc)

        if "402" in error_text or "Insufficient credits" in error_text:
            raise HTTPException(
                status_code=503,
                detail={
                    "error": "Hindsight memory service unavailable",
                    "reason": "The Hindsight memory bank has insufficient credits.",
                    "memory_source": "hindsight",
                    "action": "Add Hindsight credits and retry the operation."
                }
            )

        raise HTTPException(
            status_code=502,
            detail=f"Hindsight retain failed: {error_text}"
        )

@app.post("/api/recall")
async def recall_memory(request: RecallRequest):
    try:
        result = await memory.recall(request.query)
        memories = normalize_recall_results(result)
        return {"status":"recalled", "memory_source":"hindsight", "query":request.query, "count":len(memories), "memories":memories}
    except Exception as exc:
        error_text = str(exc)

        if "402" in error_text or "Insufficient credits" in error_text:
            raise HTTPException(
                status_code=503,
                detail={
                    "error": "Hindsight memory service unavailable",
                    "reason": "The Hindsight memory bank has insufficient credits.",
                    "memory_source": "hindsight",
                    "action": "Add Hindsight credits and retry the operation."
                }
            )

        raise HTTPException(
            status_code=502,
            detail=f"Hindsight recall failed: {error_text}"
        )

@app.post("/api/analyze-event")
async def analyze_event(event: EventRequest):
    query = " ".join(p for p in [event.event_type, event.vendor, event.location, event.description] if p)
    try:
        result = await memory.recall(query)
        recalled = normalize_recall_results(result)
    except Exception as exc:
        error_text = str(exc)

        if "402" in error_text or "Insufficient credits" in error_text:
            raise HTTPException(
                status_code=503,
                detail={
                    "error": "Hindsight memory service unavailable",
                    "reason": "The Hindsight memory bank has insufficient credits.",
                    "memory_source": "hindsight",
                    "action": "Add Hindsight credits and retry the operation."
                }
            )

        raise HTTPException(
            status_code=502,
            detail=f"Hindsight recall failed: {error_text}"
        )

    if not recalled:
        return {
            "status":"no_history", "memory_source":"hindsight", "event":event.model_dump(),
            "risk_level":"Low",
            "recommendation":"No relevant Hindsight memories were found. Use standard event preparation procedures and record the outcome so the agent can learn.",
            "why":{"current_event":{"event_type":event.event_type,"attendance":event.attendance,"vendor":event.vendor,"location":event.location},"matched_memories":[],"pattern":"No recalled operational history matched this event."}
        }

    best = recalled[0]
    outcome = str(best.get("outcome") or "").lower()
    risk = "High" if any(x in outcome for x in ["failed","failure","unsuccessful"]) else "Medium"
    recommendation = best.get("lesson") or best.get("text") or "Review the recalled operational history before proceeding."
    matched = [{"event_id":m.get("event_id"),"problem":m.get("problem"),"action":m.get("action"),"outcome":m.get("outcome"),"lesson":m.get("lesson"),"text":m.get("text"),"match_score":m.get("score"),"source":"hindsight"} for m in recalled[:5]]
    return {
        "status":"history_found", "memory_source":"hindsight", "event":event.model_dump(), "risk_level":risk,
        "recommendation":recommendation,
        "why": {"current_event":{"event_type":event.event_type,"attendance":event.attendance,"vendor":event.vendor,"location":event.location},"matched_memories":matched,"pattern":"Hindsight recalled relevant operational experience from previous events. The recalled outcome and lesson are being used to guide the current recommendation."}
    }

@app.get("/api/memories")
async def get_memories():
    try:
        result = await memory.recall("eventops operational history incidents vendors actions outcomes lessons")
        memories = normalize_recall_results(result)
        return {"status":"success", "memory_source":"hindsight", "count":len(memories), "memories":memories}
    except Exception as exc:
        error_text = str(exc)

        if "402" in error_text or "Insufficient credits" in error_text:
            raise HTTPException(
                status_code=503,
                detail={
                    "error": "Hindsight memory service unavailable",
                    "reason": "The Hindsight memory bank has insufficient credits.",
                    "memory_source": "hindsight",
                    "action": "Add Hindsight credits and retry the operation."
                }
            )

        raise HTTPException(
            status_code=502,
            detail=f"Hindsight recall failed: {error_text}"
        )

def serialize_result(result):
    if result is None: return None
    if hasattr(result, "model_dump"): return result.model_dump()
    if hasattr(result, "__dict__"): return result.__dict__
    return str(result)

def normalize_recall_results(result):
    raw = getattr(result, "results", None)
    if raw is None and isinstance(result, dict): raw = result.get("results", [])
    if raw is None: raw = []
    normalized = []
    for index, item in enumerate(raw, 1):
        text = getattr(item, "text", None) if not isinstance(item, dict) else item.get("text", "")
        score = getattr(item, "score", None) if not isinstance(item, dict) else item.get("score")
        item_id = getattr(item, "id", None) if not isinstance(item, dict) else item.get("id")
        parsed = {}
        if text:
            try:
                candidate = json.loads(text)
                if isinstance(candidate, dict): parsed = candidate
            except (json.JSONDecodeError, TypeError):
                pass
        normalized.append({
            "memory_id": item_id,
            "event_id": parsed.get("event_id"),
            "problem": parsed.get("problem"),
            "action": parsed.get("action"),
            "outcome": parsed.get("outcome"),
            "lesson": parsed.get("lesson"),
            "text": text or "",
            "score": score if score is not None else max(1, 100-index),
            "source":"hindsight"
        })
    return normalized
