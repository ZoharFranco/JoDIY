from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl


class JobSeekerUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    website: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
