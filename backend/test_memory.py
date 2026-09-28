import os
import asyncio
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

async def main():
    client = Hindsight(
        base_url=os.getenv("HINDSIGHT_API_URL"),
        api_key=os.getenv("HINDSIGHT_API_KEY")
    )

    bank_id = os.getenv("HINDSIGHT_BANK_ID")

    event_memory = """
Event: Technology Conference 2026

Attendance: 3000 people

Incident:
The AV vendor arrived late because the loading dock was congested.

Action taken:
The operations team moved the AV vendor arrival time 60 minutes earlier
for the next event.

Outcome:
Successful. The earlier arrival gave the AV team enough setup time.

Lesson learned:
For large technology conferences, AV vendors should arrive at least
60 minutes earlier when loading dock congestion is expected.

Vendor:
AV Solutions

Location:
East Loading Dock
"""

    try:
        result = await client.aretain(
            bank_id=bank_id,
            content=event_memory,
            context="EventOps operational incident and lesson learned",
            tags=["eventops", "av", "vendor", "loading-dock", "lesson"]
        )

        print("\n✅ MEMORY STORED SUCCESSFULLY!")
        print(result)

    except Exception as e:
        print("\n❌ MEMORY STORAGE FAILED")
        print(type(e).__name__)
        print(str(e))

    finally:
        await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())