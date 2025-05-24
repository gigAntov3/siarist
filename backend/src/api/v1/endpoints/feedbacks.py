from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas.feedbacks import (
    FeedbackAddSchema, 
    AnswerFeedbackAddSchema, 
    FeedbackSchema, 
    AnswerFeedbackSchema,
    AnswerFeedbacksSchema, 
)

from services.feedbacks import FeedbacksService

from api.v1.dependencies.feedbacks import feedbacks_service


router = APIRouter(
    prefix="/feedbacks",
    tags=["Feedbacks"],
)


@router.post("/")
async def add_feedback(
    feedback: FeedbackAddSchema, 
    feedbacks_service: FeedbacksService = Depends(feedbacks_service)
) -> AnswerFeedbackAddSchema:
    feedback_id = await feedbacks_service.add_feedback(feedback)
    return AnswerFeedbackAddSchema(ok=True, message="Feedback added", feedback_id=feedback_id)


@router.get("/{feedback_id}")
async def get_feedback(
    feedback_id: int, 
    feedbacks_service: FeedbacksService = Depends(feedbacks_service)
) -> AnswerFeedbackSchema:
    feedback = await feedbacks_service.get_feedback(feedback_id)
    return AnswerFeedbackSchema(ok=True, message="Feedback retrieved", feedback=feedback)


@router.get("")
async def get_feedbacks(
    feedbacks_service: FeedbacksService = Depends(feedbacks_service),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
) -> AnswerFeedbacksSchema:
    feedbacks = await feedbacks_service.get_feedbacks(limit=limit, offset=offset)
    return AnswerFeedbacksSchema(ok=True, message="Feedbacks retrieved", feedbacks=feedbacks)