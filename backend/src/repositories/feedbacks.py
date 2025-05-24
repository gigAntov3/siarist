from utils.repository import SQLAlchemyRepository

from models.feedbacks import FeedbackModel


class FeedbackRepository(SQLAlchemyRepository):
    model = FeedbackModel