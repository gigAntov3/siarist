from pydantic import BaseModel


class AnswerSchema(BaseModel):
    ok: bool
    message: str
