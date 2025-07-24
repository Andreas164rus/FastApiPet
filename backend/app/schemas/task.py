from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskBase(BaseModel):
    title: str
    description: Optional[str]
    status: StatusEnum


class TaskCreate(TaskBase):
    pass


class TaskDB(TaskBase):
    id: int
    created: datetime
    
    class Config:
        orm_mode = True
