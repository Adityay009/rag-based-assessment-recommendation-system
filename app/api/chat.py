from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.request_models import ChatRequest
from app.services.recommender import RecommenderService

router = APIRouter()

recommender = RecommenderService()


class Message(BaseModel):
    role: str
    content: str


class APIChatRequest(BaseModel):
    messages: List[Message]


def get_test_type(keys: List[str]) -> str:
    """
    Convert SHL category to assignment test_type.
    """

    mapping = {
        "Knowledge & Skills": "K",
        "Personality & Behavior": "P",
        "Ability & Aptitude": "A",
        "Competencies": "C",
        "Biodata & Situational Judgment": "S",
        "Assessment Exercises": "E",
        "Development & 360": "D",
    }

    if not keys:
        return "U"

    return mapping.get(keys[0], "U")


@router.post("/chat")
def chat(request: APIChatRequest):

    latest_user_message = ""

    for message in reversed(request.messages):
        if message.role == "user":
            latest_user_message = message.content
            break

    internal_request = ChatRequest(
        message=latest_user_message,
        conversation_history=[
            f"{m.role}: {m.content}"
            for m in request.messages[:-1]
        ],
    )

    result = recommender.recommend(internal_request)

    recommendations = []

    for rec in result.recommendations:
        recommendations.append(
            {
                "name": rec.name,
                "url": rec.link,
                "test_type": get_test_type(rec.keys),
            }
        )

    return {
        "reply": result.response,
        "recommendations": recommendations,
        "end_of_conversation": result.end_of_conversation,
}


@router.get("/health")
def health():
    return {
        "status": "ok"
    }