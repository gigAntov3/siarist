from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class FileSchema(BaseModel):
    file_name: str
    url: str

    class Config:
        from_attributes = True


class AnswerFileSchema(BaseModel):
    ok: bool
    message: str
    file: Optional[FileSchema]