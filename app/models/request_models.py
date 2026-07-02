from typing import List, Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Internal request model used by the recommender.
    """

    message: str = Field(
        ...,
        description="User message."
    )

    conversation_history: Optional[List[str]] = Field(
        default_factory=list
    )