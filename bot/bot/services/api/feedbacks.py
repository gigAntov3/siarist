import asyncio
import aiohttp

from typing import List

from bot.services.api.schemas import Answer
from bot.services.api.schemas.feedbacks import (
    FeedbackSchema,
    AnswerFeedbacksSchema,
    AnswerFeedbackSchema,
    AnswerFeedbackAdd
)


class FeedbacksAPI:
    BASE_URL = "http://127.0.0.1:8000/feedbacks"


    async def get_feedbacks(self, limit: int = 1, offset: int  = 0) -> List[FeedbackSchema]:
        url = "http://127.0.0.1:8000/feedbacks"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params={"limit": limit, "offset": offset}) as response:
                return AnswerFeedbacksSchema(**await response.json()).feedbacks
            
    
    async def get_feedback(self, id: int) -> FeedbackSchema:
        url = f"http://127.0.0.1:8000/feedbacks/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return AnswerFeedbackSchema(**await response.json()).feedback
            

    async def delete_feedback(self, id: int) -> Answer:
        url = f"http://127.0.0.1:8000/feedbacks/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                return Answer(**await response.json())
            

    async def add_feedback(self, content: str, priority: int, author_id: int) -> int:
        url = "http://127.0.0.1:8000/feedbacks/"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={"content": content, "priority": priority, "author_id": author_id}) as response:
                return AnswerFeedbackAdd(**await response.json()).feedback_id
            

if __name__ == "__main__":
    api = FeedbacksAPI()
    asyncio.run(api.get_feedbacks(limit=3, offset=0))