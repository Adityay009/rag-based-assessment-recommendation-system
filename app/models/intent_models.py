from typing import List

from pydantic import BaseModel


class UserIntent(BaseModel):
    """
    Structured intent extracted from the user's query.
    """

    role: str = ""

    skills: List[str] = []

    experience: str = ""

    job_level: str = ""

    # NEW FIELD
    purpose: str = ""

    remote: str = ""

    adaptive: str = ""