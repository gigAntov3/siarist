from typing import List, Optional, Union, Dict, Any, Literal 

from datetime import datetime

from pydantic import BaseModel


class File(BaseModel):
    file_name: str
    url: str
    
    class Config:
        from_attributes = True


class AnswerFileAdd(BaseModel):
    ok: bool
    message: str
    file: File

    class Config:
        from_attributes = True