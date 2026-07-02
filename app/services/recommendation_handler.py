from app.models.response_models import (
    ChatResponse,
    AssessmentRecommendation,
)


class RecommendationHandler:
    """
    Handles new recommendation requests.
    """

    def build_response(
        self,
        response_text: str,
        retrieved: list,
    ) -> ChatResponse:

        recommendations = []

        for item in retrieved:

            recommendations.append(
                AssessmentRecommendation(
                    name=item["name"],
                    link=item["link"],
                    duration=item["duration"],
                    description=item["description"],
                    similarity_score=item["similarity_score"],
                    keys=item.get("keys", []),
                )
            )

        return ChatResponse(
            response=response_text,
            recommendations=recommendations,
            follow_up_question=None,
            end_of_conversation=False
        )