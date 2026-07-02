from app.services.intent_extractor import IntentExtractor

extractor = IntentExtractor()

print(
    extractor.extract(
        "Looking for a Java backend developer with 4 years experience"
    )
)