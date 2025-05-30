from typing import List
from datetime import datetime
from pydantic import BaseModel

from .users import User


class FeedbackSchema(BaseModel):
    id: int
    content: str
    priority: int
    author: User
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AnswerFeedbackSchema(BaseModel):
    ok: bool
    message: str
    feedback: FeedbackSchema


class FeedbacksSchema(BaseModel):
    feedbacks: List[FeedbackSchema]

    class Config:
        from_attributes = True


class AnswerFeedbacksSchema(BaseModel):
    ok: bool
    message: str
    feedbacks: List[FeedbackSchema]


class AnswerFeedbackAdd(BaseModel):
    ok: bool
    message: str
    feedback_id: int