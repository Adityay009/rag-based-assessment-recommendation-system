from app.models.response_models import ChatResponse


class RefinementHandler:
    """
    Handles requests to refine an existing assessment shortlist.
    """

    def refine(
        self,
        message: str,
        previous_recommendations: list,
    ) -> ChatResponse:

        message_lower = message.lower()

        if "cognitive" in message_lower:
            response = (
                "Understood. I'll update the shortlist by adding an appropriate "
                "cognitive assessment while keeping the existing recommendations."
            )

        elif "replace" in message_lower:
            response = (
                "Understood. I'll replace the requested assessment with the "
                "closest suitable alternative from the SHL catalog, if one exists."
            )

        elif "remove" in message_lower:
            response = (
                "Understood. I'll remove the requested assessment and update "
                "the shortlist."
            )

        elif "shorter" in message_lower:
            response = (
                "Understood. I'll look for shorter assessments that provide "
                "similar coverage where possible."
            )

        elif "remote" in message_lower:
            response = (
                "Understood. I'll prioritize assessments that support remote "
                "administration."
            )

        else:
            response = (
                "Understood. I'll refine the assessment shortlist based on "
                "your latest requirements."
            )

        return ChatResponse(
            response=response,
            recommendations=previous_recommendations,
            follow_up_question=None,
            end_of_conversation=False
        )