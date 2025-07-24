from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from datetime import datetime
from app.core.db import Base

class Task(Base):

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum("pending", "in_progress", "done", name="status_types"), default="pending") 
    created = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('user.id'))