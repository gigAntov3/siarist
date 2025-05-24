from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

# Отложенный импорт для типизации, чтобы избежать циклических импортов
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import UserModel

from schemas.feedbacks import FeedbackSchema


class FeedbackModel(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str]
    priority: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship(
        "UserModel",
        back_populates="feedbacks"
    )

    def to_read_model(self) -> FeedbackSchema:
        return FeedbackSchema(
            id=self.id,
            content=self.content,
            priority=self.priority,
            author_id=self.author_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
