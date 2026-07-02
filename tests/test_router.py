from app.services.conversation_router import (
    ConversationRouter,
)

router = ConversationRouter()

tests = [

    "Need a Java developer",

    "Add a cognitive test",

    "Compare OPQ32r and Verify G+",

    "Confirmed",

    "We'll use Safety & Dependability 8.0",

    "Proceed",

    "Thanks",

    "Goodbye",

]

for test in tests:

    print(test)

    print(router.detect_mode(test))

    print("-" * 40)