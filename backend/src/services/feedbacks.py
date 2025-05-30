from typing import Optional

from utils.repository import BaseRepository
from schemas.feedbacks import FeedbackAddSchema


class FeedbacksService:
    def __init__(self, feedbacks_repo: BaseRepository):
        self.feedbacks_repo = feedbacks_repo()

    async def add_feedback(self, feedback: FeedbackAddSchema):
        feedback_dict = feedback.model_dump()
        feedback_id = await self.feedbacks_repo.add_one(feedback_dict)
        return feedback_id
    

    async def get_feedback(self, feedback_id: int):
        feedback = await self.feedbacks_repo.find_one(id=feedback_id)
        return feedback
    

    async def get_feedbacks(self, limit: Optional[int] = None, offset: Optional[int] = None):
        feedbacks = await self.feedbacks_repo.find_all(limit=limit, offset=offset, order_by="priority")
        return feedbacks
    

    async def delete_feedback(self, feedback_id: int):
        await self.feedbacks_repo.delete_one(id=feedback_id)