
from datetime import datetime
from pydantic import BaseModel


class UserAddSchema(BaseModel):
    chat_id: int
    first_name: str
    last_name: str | None
    username: str | None
    balance: int

    class Config:
        from_attributes = True


class AnswerUserAddSchema(BaseModel):
    ok: bool
    message: str
    user_id: int

    class Config:
        from_attributes = True


class UserSchema(UserAddSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AnswerUserSchema(BaseModel):
    ok: bool
    message: str
    user: UserSchema

    class Config:
        from_attributes = True


class AnswerUsersSchema(BaseModel):
    ok: bool
    message: str
    users: list[UserSchema]

    class Config:
        from_attributes = True