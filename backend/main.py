from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

from memory.memory_store import (
    search_memories,
    store_memory,
    get_memories
)


app = FastAPI(
    title="EventOps Memory Agent",
    description=(
        "AI-powered event operations intelligence system "
        "with long-term operational memory."
    ),
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EventRequest(BaseModel):
    event_type: str = Field(min_length=1)
    attendance: int = Field(gt=0)
    vendor: str = ""
    location: str = ""
    event_time: str = ""
    description: str = ""

    @field_validator(
        "event_type",
        "vendor",
        "location",
        "event_time",
        "description",
        mode="before"
    )
    @classmethod
    def clean_text(cls, value):
        if value is None:
            return ""

        return str(value).strip()


class OutcomeRequest(BaseModel):
    event_id: str = Field(min_length=1)
    outcome: str = Field(min_length=1)
    actual_problem: str = Field(min_length=1)
    action_taken: str = Field(min_length=1)
    lesson_learned: str = Field(min_length=1)

    @field_validator(
        "event_id",
        "outcome",
        "actual_problem",
        "action_taken",
        "lesson_learned",
        mode="before"
    )
    @classmethod
    def clean_required_text(cls, value):

        if value is None:
            raise ValueError("This field is required.")

        value = str(value).strip()

        if not value:
            raise ValueError("This field cannot be empty.")

        return value


@app.get("/")
def home():

    return {
        "status": "online",
        "agent": "EventOps Memory Agent",
        "version": "1.0"
    }


@app.get("/api/health")
def health():

    return {
        "status": "healthy",
        "service": "EventOps Backend"
    }


@app.get("/api/memories")
def get_all_memories():

    memories = get_memories()

    return {
        "status": "success",
        "count": len(memories),
        "memories": memories
    }


@app.post("/api/analyze-event")
def analyze_event(event: EventRequest):

    query_parts = [
        event.event_type,
        event.vendor,
        event.location,
        event.description
    ]

    query = " ".join(
        part
        for part in query_parts
        if part
    )

    memories = search_memories(query)

    relevant_memories = [
        item
        for item in memories
        if item["score"] >= 2
    ][:5]

    if not relevant_memories:

        return {
            "status": "no_history",
            "event": event.model_dump(),
            "risk_level": "Low",
            "recommendation": (
                "No relevant historical incidents were found. "
                "Use standard event preparation procedures and "
                "capture the event outcome so the agent can learn "
                "from this event."
            ),
            "why": {
                "current_event": {
                    "event_type": event.event_type,
                    "attendance": event.attendance,
                    "vendor": event.vendor,
                    "location": event.location
                },
                "matched_memories": [],
                "pattern": None
            }
        }

    best_match = relevant_memories[0]["memory"]

    previous_outcome = str(
        best_match.get("outcome", "")
    ).lower()

    if previous_outcome in [
        "failed",
        "failure",
        "unsuccessful"
    ]:

        risk_level = "High"

    elif previous_outcome in [
        "successful",
        "success"
    ]:

        risk_level = "Medium"

    else:

        risk_level = "Medium"


    recommendation = best_match.get(
        "lesson",
        "Review the previous event before proceeding."
    )


    matched_memories = []

    for item in relevant_memories:

        memory = item["memory"]

        matched_memories.append(
            {
                "event_id": memory.get("event_id"),
                "problem": memory.get("problem"),
                "action": memory.get("action"),
                "outcome": memory.get("outcome"),
                "lesson": memory.get("lesson"),
                "match_score": item["score"]
            }
        )


    why = {

        "current_event": {
            "event_type": event.event_type,
            "attendance": event.attendance,
            "vendor": event.vendor,
            "location": event.location
        },

        "matched_memories": matched_memories,

        "pattern": (
            "A similar operational situation occurred in a "
            "previous event. The historical outcome and lesson "
            "are being used to guide the current event "
            "recommendation."
        )
    }


    return {

        "status": "history_found",

        "event": event.model_dump(),

        "risk_level": risk_level,

        "recommendation": recommendation,

        "why": why
    }


@app.post("/api/outcome")
def record_outcome(outcome: OutcomeRequest):

    existing_memories = get_memories()


    # Prevent exact duplicate memories

    for memory in existing_memories:

        same_event = (
            memory.get("event_id")
            == outcome.event_id
        )

        same_problem = (
            memory.get("problem")
            == outcome.actual_problem
        )

        same_action = (
            memory.get("action")
            == outcome.action_taken
        )

        same_outcome = (
            memory.get("outcome")
            == outcome.outcome
        )

        same_lesson = (
            memory.get("lesson")
            == outcome.lesson_learned
        )


        if (
            same_event
            and same_problem
            and same_action
            and same_outcome
            and same_lesson
        ):

            return {

                "status": "already_exists",

                "message": (
                    "This operational outcome "
                    "is already stored."
                ),

                "memory": memory
            }


    memory = {

        "event_id": outcome.event_id,

        "problem": outcome.actual_problem,

        "action": outcome.action_taken,

        "outcome": outcome.outcome,

        "lesson": outcome.lesson_learned,

        "tags": [
            "eventops",
            "outcome",
            "learned-lesson"
        ]
    }


    stored_memory = store_memory(memory)


    return {

        "status": "learned",

        "message": (
            "Event outcome successfully stored "
            "as a new operational memory."
        ),

        "memory": stored_memory
    }