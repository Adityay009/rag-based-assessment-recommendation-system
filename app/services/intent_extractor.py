import re
from typing import Dict


TECH_SKILLS = [
    "python",
    "java",
    "c++",
    "c",
    "sql",
    "spring",
    "spring boot",
    "hibernate",
    "javascript",
    "react",
    "node",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "linux",
    "git",
]


ROLES = [
    "backend developer",
    "frontend developer",
    "full stack developer",
    "software engineer",
    "developer",
    "data scientist",
    "data analyst",
    "machine learning engineer",
    "devops engineer",
    "qa engineer",
    "tester",
    "architect",
    "manager",
    "director",
    "executive",
    "cxo",
    "leadership",
]


PURPOSE_KEYWORDS = {
    "selection": [
        "selection",
        "hiring",
        "recruitment",
        "benchmark",
        "candidate",
        "compare candidates",
    ],
    "development": [
        "development",
        "developmental",
        "coach",
        "coaching",
        "feedback",
    ],
    "promotion": [
        "promotion",
        "promote",
    ],
    "succession": [
        "succession",
        "successor",
        "succession planning",
    ],
}


class IntentExtractor:

    def extract(self, text: str) -> Dict:

        text_lower = text.lower()

        intent = {
            "role": "",
            "skills": [],
            "experience": "",
            "job_level": "",
            "purpose": "",
            "remote": "",
            "adaptive": "",
        }

        # ---------------------------
        # Role
        # ---------------------------
        for role in ROLES:
            if role in text_lower:
                intent["role"] = role
                break

        # Special handling for senior leadership
        if (
            "senior leadership" in text_lower
            or "executive leadership" in text_lower
        ):
            intent["role"] = "senior leadership"

        # ---------------------------
        # Skills
        # ---------------------------

        for skill in TECH_SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text_lower):

                intent["skills"].append(skill)

        # ---------------------------
        # Experience
        # ---------------------------
        match = re.search(r"(\d+)\s*(?:\+)?\s*years?", text_lower)

        if match:
            intent["experience"] = match.group(1)

        # ---------------------------
        # Job Level
        # ---------------------------
        if "entry" in text_lower or "junior" in text_lower:
            intent["job_level"] = "Entry-Level"

        elif "mid" in text_lower:
            intent["job_level"] = "Mid-Level"

        elif "senior" in text_lower:
            intent["job_level"] = "Senior"

        # ---------------------------
        # Purpose
        # ---------------------------
        for purpose, keywords in PURPOSE_KEYWORDS.items():

            for keyword in keywords:

                if keyword in text_lower:
                    intent["purpose"] = purpose
                    break

            if intent["purpose"]:
                break

        # ---------------------------
        # Remote
        # ---------------------------
        if "remote" in text_lower:
            intent["remote"] = "Yes"

        # ---------------------------
        # Adaptive
        # ---------------------------
        if "adaptive" in text_lower:
            intent["adaptive"] = "Yes"

        return intent