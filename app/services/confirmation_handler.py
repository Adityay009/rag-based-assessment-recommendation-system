from app.models.response_models import ChatResponse


class ConfirmationHandler:
    """
    Handles confirmation of the recommended assessment shortlist.
    """

    def confirm(
        self,
        previous_recommendations: list,
    ) -> ChatResponse:

        if previous_recommendations:

            response = (
                "Great! Based on your requirements, these assessments form a "
                "strong shortlist for evaluating your candidates. "
                "You can review the assessment details using the provided SHL "
                "links and proceed with your hiring process."
            )

        else:

            response = (
                "Great! Your assessment selection has been confirmed. "
                "If you need help refining or comparing assessments later, "
                "I'm happy to help."
            )

        return ChatResponse(
            response=response,
            recommendations=previous_recommendations,
            follow_up_question=None,
            end_of_conversation=True,
        )