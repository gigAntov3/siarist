from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from datetime import datetime

BaseUsers = declarative_base()

# Модель пользователя
class User(BaseUsers):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, chat_id='{self.chat_id}', first_name='{self.first_name}', username='{self.username}', created_at='{self.created_at}')>"
