from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    src: str
    rating: Optional[float] = Field(default=None)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
