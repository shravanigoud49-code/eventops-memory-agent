import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

class HindsightMemory:
    def __init__(self):
        self.base_url = os.getenv("HINDSIGHT_API_URL")
        self.api_key = os.getenv("HINDSIGHT_API_KEY")
        self.bank_id = os.getenv("HINDSIGHT_BANK_ID")
        if not self.base_url:
            raise RuntimeError("HINDSIGHT_API_URL is missing from .env")
        if not self.bank_id:
            raise RuntimeError("HINDSIGHT_BANK_ID is missing from .env")
        kwargs = {"base_url": self.base_url}
        if self.api_key:
            kwargs["api_key"] = self.api_key
        self.client = Hindsight(**kwargs)

    async def version(self):
        result = await self.client.aget_version()
        return getattr(result, "api_version", None) or str(result)

    async def retain_event(self, content: str):
        return await self.client.aretain(
            bank_id=self.bank_id,
            content=content,
            context="EventOps operational event outcome",
        )

    async def recall(self, query: str):
        return await self.client.arecall(bank_id=self.bank_id, query=query)
