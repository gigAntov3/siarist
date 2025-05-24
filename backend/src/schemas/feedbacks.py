from typing import List
from datetime import datetime
from pydantic import BaseModel


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


class FeedbackSchema(FeedbackAddSchema):
    id: int
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