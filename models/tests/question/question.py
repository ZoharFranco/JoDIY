from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class Question(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    text: str
    category: Optional[str] = None
