from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr # automatic email validation
    major: str
    gpa: float
    enrollment_year: int