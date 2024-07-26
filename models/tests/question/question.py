from datetime import datetime, timezone
from enum import Enum
from typing import List
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class QuestionCategory(Enum):
    ALGORITHMS = "algorithms"


class QuestionDifficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Question(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    category: QuestionCategory = None
    difficulty: QuestionDifficulty

    text: str
    examples: List[str]
