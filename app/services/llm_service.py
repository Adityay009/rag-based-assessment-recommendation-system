import json
import os
import re

from dotenv import load_dotenv
from google import genai

from app.models.intent_models import UserIntent
from app.prompts.system_prompt import (
    INTENT_EXTRACTION_PROMPT,
    RECOMMENDATION_PROMPT,
)

load_dotenv()


class LLMService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    def _clean_json(self, text: str) -> str:
        """Remove markdown formatting from Gemini JSON output."""
        text = text.strip()
        text = re.sub(r"^```json\s*", "", text)
        text = re.sub(r"^```\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()

    def _generate(self, prompt: str):
        """
        Try multiple Gemini models in case one is unavailable.
        """
        models = [
            "gemini-2.0-flash",
            "gemini-2.5-flash",
        ]

        last_error = None

        for model in models:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                return response

            except Exception as e:
                print(f"⚠️ {model} failed: {e}")
                last_error = e

        raise RuntimeError(f"All Gemini models failed.\n{last_error}")

    def extract_intent(self, query: str) -> UserIntent:
        prompt = f"""
{INTENT_EXTRACTION_PROMPT}

User Message:
{query}
"""

        response = self._generate(prompt)

        text = self._clean_json(response.text)

        data = json.loads(text)

        return UserIntent(**data)

    def generate_recommendation(
        self,
        query: str,
        assessments: list,
    ) -> str:

        simplified = [
            {
                "name": a["name"],
                "description": a["description"],
                "duration": a["duration"],
                "link": a["link"],
            }
            for a in assessments
        ]

        prompt = f"""
{RECOMMENDATION_PROMPT}

User Query:
{query}

Assessments:
{json.dumps(simplified, indent=2)}
"""

        response = self._generate(prompt)

        return response.text