from memory.memory_store import search_memories


query = "technology conference AV vendor loading dock"

results = search_memories(query)

print("\nMEMORY SEARCH RESULTS")
print("=" * 50)

if not results:
    print("No relevant memories found.")

else:
    for result in results:
        memory = result["memory"]

        print(f"\nScore: {result['score']}")
        print(f"Event: {memory.get('event_id')}")
        print(f"Problem: {memory.get('problem')}")
        print(f"Action: {memory.get('action')}")
        print(f"Outcome: {memory.get('outcome')}")
        print(f"Lesson: {memory.get('lesson')}")