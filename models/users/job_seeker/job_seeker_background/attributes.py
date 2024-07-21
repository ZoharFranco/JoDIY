from datetime import date
from typing import Optional, List

from pydantic import BaseModel


class Experience(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    description: Optional[str] = None


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: date
    end_date: Optional[date] = None


class Skill(BaseModel):
    name: str
    description: str
