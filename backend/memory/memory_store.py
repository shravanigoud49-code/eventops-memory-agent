import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "event_memories.json"
)


def load_memories():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_memories(memories):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memories, file, indent=2)


def store_memory(memory):
    memories = load_memories()

    memory["memory_id"] = len(memories) + 1
    memory["created_at"] = datetime.utcnow().isoformat()

    memories.append(memory)

    save_memories(memories)

    return memory


def get_memories():
    return load_memories()


def search_memories(query):
    memories = load_memories()

    query_words = set(query.lower().split())

    results = []

    for memory in memories:
        searchable_text = " ".join(
            str(value)
            for value in memory.values()
        ).lower()

        score = sum(
            1 for word in query_words
            if word in searchable_text
        )

        if score > 0:
            results.append(
                {
                    "memory": memory,
                    "score": score
                }
            )

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results