import httpx
from app.config import settings

async def generate(messages):
    url = settings.llm_base_url.rstrip("/") + "/chat/completions"
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(url, headers={"Authorization":f"Bearer {settings.llm_api_key}"}, json={
            "model":settings.llm_model,"messages":messages,"temperature":settings.llm_temperature})
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"], data.get("usage",{})
