from enum import Enum


class ConversationMode(str, Enum):

    RECOMMEND = "recommend"

    REFINE = "refine"

    COMPARE = "compare"

    CLARIFY = "clarify"

    CONFIRM = "confirm"

class ConversationRouter:
    """
    Determines what kind of user request
    this message represents.
    """

    def detect_mode(
        self,
        message: str,
    ) -> ConversationMode:

        text = message.lower()

        # -----------------------
        # Compare
        # -----------------------

        if (
            "compare" in text
            or "difference" in text
            or "vs" in text
            or "versus" in text
        ):

            return ConversationMode.COMPARE

        # -----------------------
        # Refine
        # -----------------------

        refinement_words = [

            "also",

            "add",

            "include",

            "instead",

            "remove",

            "without",

            "replace",

            "another",

            "change",

            "update",

        ]

        if any(
            word in text
            for word in refinement_words
        ):

            return ConversationMode.REFINE

        confirmation_words = [

            "confirmed",

            "confirm",

            "we'll use",

            "we will use",

            "that's the one",

            "that is the one",

            "approved",

            "proceed",
            
            # Conversation endings

            "thanks",

            "thank you",

            "thankyou",

            "thx",

            "bye",

            "goodbye",

            "see you",

            "that's all",

            "thats all",

            "all good",

            "perfect",

            "great",

            "awesome",

        ]

        if any(word in text for word in confirmation_words):

            return ConversationMode.CONFIRM

        # -----------------------
        # Default
        # -----------------------

        return ConversationMode.RECOMMEND