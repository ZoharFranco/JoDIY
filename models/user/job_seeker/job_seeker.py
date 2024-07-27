from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from models.user.job_seeker.job_seeker_background.job_seeker_background import JobSeekerBackground
from models.user.job_seeker.job_seeker_user.job_seeker_user import JobSeekerUser


class JobSeeker(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user: JobSeekerUser
    background: JobSeekerBackground
