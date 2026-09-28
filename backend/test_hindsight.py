import os
import asyncio
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

API_URL = os.getenv("HINDSIGHT_API_URL")
API_KEY = os.getenv("HINDSIGHT_API_KEY")

async def main():
    if not API_URL:
        print("ERROR: HINDSIGHT_API_URL is missing from .env")
        return

    if not API_KEY:
        print("ERROR: HINDSIGHT_API_KEY is missing from .env")
        return

    print("Connecting to Hindsight...")

    client = Hindsight(
        base_url=API_URL,
        api_key=API_KEY
    )

    try:
        response = await client.aget_version()

        print("\nSUCCESS! Hindsight connection is working.")
        print("API Version:", response.api_version)

    except Exception as e:
        print("\nCONNECTION FAILED")
        print(type(e).__name__)
        print(str(e))

    finally:
        await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())