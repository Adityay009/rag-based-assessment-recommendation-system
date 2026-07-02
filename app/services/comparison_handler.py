from app.models.response_models import ChatResponse


class ComparisonHandler:
    """
    Handles comparison requests between assessments.
    """

    def compare(
        self,
        message: str,
        previous_recommendations: list,
    ) -> ChatResponse:

        message_lower = message.lower()

        if "opq" in message_lower and "verify" in message_lower:

            response = (
                "OPQ focuses on personality, behavioural preferences, and "
                "work style, helping predict how a candidate is likely to "
                "behave in the workplace.\n\n"
                "Verify G+ measures cognitive ability, including reasoning, "
                "problem solving, and learning capability.\n\n"
                "These assessments measure different attributes and are often "
                "used together to provide a balanced evaluation of both "
                "behavioural fit and cognitive capability."
            )

        elif "compare" in message_lower:

            response = (
                "These assessments measure different competencies and are "
                "designed for different hiring objectives. Reviewing their "
                "descriptions, duration, and target competencies will help "
                "determine which best fits your hiring requirements."
            )

        else:

            response = (
                "Please specify which two assessments you would like to "
                "compare."
            )

        return ChatResponse(
            response=response,
            recommendations=previous_recommendations,
            follow_up_question=None,
            end_of_conversation=False
        )