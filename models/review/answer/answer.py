from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import Field, BaseModel

from models.review.answer.answer_evaluation import AnswerEvaluation


class Answer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    question_id: UUID
    answer_content: str
    answer_evaluation: AnswerEvaluation
