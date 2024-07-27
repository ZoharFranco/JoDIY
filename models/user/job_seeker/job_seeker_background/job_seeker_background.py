from typing import List

from pydantic import BaseModel

from models.user.job_seeker.job_seeker_background.attributes import Experience, Education, Skill


class JobSeekerBackground(BaseModel):
    experiences: List[Experience]
    education: List[Education]
    skills: List[Skill]
