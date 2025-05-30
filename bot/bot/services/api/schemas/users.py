from typing import List, Optional, Union, Dict, Any, Literal 

from datetime import datetime

from pydantic import BaseModel



class User(BaseModel):
    id: int
    chat_id: int
    first_name: str
    last_name: str
    username: str
    balance: int
    purchases_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True