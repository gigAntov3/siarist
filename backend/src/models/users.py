from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
from schemas.users import UserSchema


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int]
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
    balance: Mapped[int] = mapped_column(default=0)
    purchases_count: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    # Связь с отзывами — обратная сторона отношений (FeedbackModel должен быть определён и импортирован)
    feedbacks = relationship(
        "FeedbackModel",           # строка с именем модели для отложенной загрузки
        back_populates="author",   # имя обратной связи в FeedbackModel
        cascade="all, delete-orphan"
    )

    orders = relationship("OrderModel", back_populates="user", cascade="all, delete-orphan")

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            chat_id=self.chat_id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            balance=self.balance,
            purchases_count=self.purchases_count,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
