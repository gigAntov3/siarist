from typing import List
from datetime import datetime
from pydantic import BaseModel

from .users import UserSchema


class FeedbackAddSchema(BaseModel):
    content: str
    priority: int
    author_id: int

    class Config:
        orm_mode = True


class AnswerFeedbackAddSchema(BaseModel):
    ok: bool
    message: str
    feedback_id: int


class FeedbackSchema(BaseModel):
    id: int
    content: str
    priority: int
    author: UserSchema
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class AnswerFeedbackSchema(BaseModel):
    ok: bool
    message: str
    feedback: FeedbackSchema


class AnswerFeedbacksSchema(BaseModel):
    ok: bool
    message: str
    feedbacks: List[FeedbackSchema]