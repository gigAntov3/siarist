from pydantic import BaseModel

class Answer(BaseModel):
    ok: bool
    message: str