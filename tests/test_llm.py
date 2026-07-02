from app.services.llm_service import LLMService

llm = LLMService()

intent = llm.extract_intent(
    "Looking for a Java backend developer with 4 years experience"
)

print(intent)