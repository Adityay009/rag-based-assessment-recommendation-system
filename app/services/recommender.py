from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from app.services.catalog_analyzer import CatalogAnalyzer
from app.services.confirmation_handler import ConfirmationHandler
from app.services.conversation_router import (
    ConversationMode,
    ConversationRouter,
)
from app.services.intent_extractor import IntentExtractor
from app.services.llm_service import LLMService
from app.services.recommendation_handler import RecommendationHandler
from app.services.retriever import Retriever
from app.services.refinement_handler import RefinementHandler
from app.services.comparison_handler import ComparisonHandler


class RecommenderService:
    """
    Main orchestrator for the recommendation pipeline.
    """

    def __init__(self):

        self.intent_extractor = IntentExtractor()

        self.llm = LLMService()

        self.retriever = Retriever()

        self.catalog = CatalogAnalyzer()

        self.router = ConversationRouter()

        self.recommendation_handler = RecommendationHandler()

        self.confirmation_handler = ConfirmationHandler()
        
        self.refinement_handler = RefinementHandler()
        
        self.comparison_handler = ComparisonHandler()

    def recommend(
        self,
        request: ChatRequest,
) -> ChatResponse:
        """
        Main recommendation pipeline.
        """

        conversation = self._build_conversation(request)
        latest_message = request.message

        mode = self.router.detect_mode(latest_message)

# Conversation handlers

        if mode == ConversationMode.COMPARE:

            return self.comparison_handler.compare(
                latest_message,
                [],
            )

        if mode == ConversationMode.REFINE:

            return self.refinement_handler.refine(
                latest_message,
                [],
            )

        if mode == ConversationMode.CONFIRM:

            return self.confirmation_handler.confirm(
                [],
            )

        intent, unsupported_skills = self._extract_intent(
        conversation
    )

        follow_up = self._get_follow_up_question(intent)

        if follow_up:

            return ChatResponse(
            response=follow_up,
            recommendations=[],
            follow_up_question=follow_up,
            )

        retrieved = self._retrieve_assessments(
            intent,
            unsupported_skills,
    )

        recommendation_text = self.llm.generate_recommendation(
            request.message,
            retrieved,
    )

        if unsupported_skills:

            recommendation_text = (
                f"SHL doesn't currently offer a dedicated assessment for "
                f"{', '.join(unsupported_skills)}.\n\n"
                + recommendation_text
            )

        return self.recommendation_handler.build_response(
            response_text=recommendation_text,
            retrieved=retrieved,
    )
        
    def _build_conversation(
        self,
        request: ChatRequest,
) -> str:

        conversation = ""

        if (
            hasattr(request, "conversation_history")
            and request.conversation_history
        ):
            conversation = "\n".join(
                request.conversation_history
            )

        conversation += f"\nUser: {request.message}"

        return conversation
    
    def _extract_intent(
        self,
        conversation: str,
):

        intent = self.intent_extractor.extract(
            conversation
        )

        unsupported_skills = []

        for skill in intent["skills"]:

            if not self.catalog.is_supported(skill):

                unsupported_skills.append(skill)

        return intent, unsupported_skills
    
    def _retrieve_assessments(
        self,
        intent,
        unsupported_skills,
):

        retrieval_query = self._build_search_query(
            intent
    )

        if unsupported_skills:

            retrieval_query += (
                " Linux Networking "
                " Systems Programming "
                " Live Coding "
        )

        filters = self._build_filters(intent)

        return self.retriever.retrieve(
            query=retrieval_query,
            filters=filters,
    )

    def _build_search_query(self, intent) -> str:
        """
        Build semantic search query.
        """

        parts = []

        if intent["role"]:
            parts.append(intent["role"])

        if intent["skills"]:
            parts.extend(intent["skills"])

        if intent["experience"]:
            parts.append(intent["experience"])

        return " ".join(parts)

    def _build_filters(self, intent):
        """
        Build metadata filters.
        """

        filters = {}

        if intent["remote"]:
            filters["remote"] = intent["remote"]

        if intent["adaptive"]:
            filters["adaptive"] = intent["adaptive"]

        return filters

    def _get_follow_up_question(self, intent):
        """
        Ask only for the missing information required
        to make a good recommendation.
        """

        if not intent["role"]:
            return (
            "Who is this assessment intended for? "
            "For example: Software Developer, Data Scientist, Senior Leadership, Sales Manager."
        )

        if intent["role"] == "senior leadership" and not intent["purpose"]:
            return (
            "Is this for selection, leadership benchmarking, succession planning, or employee development?"
        )

        if (
        intent["role"] != "senior leadership"
        and len(intent["skills"]) == 0
    ):
            return (
            "What key skills would you like to assess? "
            "For example: Java, Python, SQL, Leadership."
        )

        return None
    
    