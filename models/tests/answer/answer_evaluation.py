from dataclasses import Field
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class AnswerEvaluation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    question_id: UUID
    correction: bool
    feedback: Optional[str] = None
    score: Optional[float] = None
