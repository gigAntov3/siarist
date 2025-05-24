from services.feedbacks import FeedbacksService
from repositories.feedbacks import FeedbackRepository


def feedbacks_service():
    return FeedbacksService(FeedbackRepository)