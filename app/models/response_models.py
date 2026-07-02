from typing import List, Optional

from pydantic import BaseModel


class AssessmentRecommendation(BaseModel):
    """
    One recommended assessment.
    """

    name: str
    link: str
    duration: str
    description: str
    similarity_score: float

    keys: List[str]


class ChatResponse(BaseModel):
    """
    Response returned by the recommender.
    """

    response: str

    recommendations: List[AssessmentRecommendation]

    follow_up_question: Optional[str] = None
    
class ChatResponse(BaseModel):

    response: str

    recommendations: List[AssessmentRecommendation]

    follow_up_question: Optional[str] = None

    end_of_conversation: bool = False