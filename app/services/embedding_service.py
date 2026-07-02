from typing import Dict, List

import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Responsible for converting SHL assessments into vector embeddings.
    """

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):

        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        print("Embedding model loaded successfully.\n")

    def build_document(self, assessment: Dict) -> str:
        """
        Creates a natural language representation of an assessment
        for better semantic embeddings.
        """

        name = assessment.get("name", "")
        description = assessment.get("description", "")
        categories = ", ".join(assessment.get("keys", []))
        job_levels = ", ".join(assessment.get("job_levels", []))
        languages = ", ".join(assessment.get("languages", []))
        duration = assessment.get("duration", "")
        remote = assessment.get("remote", "")
        adaptive = assessment.get("adaptive", "")

        document = f"""
{name} is an SHL assessment.

Description:
{description}

This assessment evaluates the following competencies:
{categories}.

It is suitable for candidates at these job levels:
{job_levels}.

The assessment duration is {duration}.

Languages available:
{languages}.

Remote testing supported: {remote}.

Adaptive assessment: {adaptive}.
"""

        return " ".join(document.split())

    def build_documents(
        self,
        catalog: List[Dict]
    ) -> List[str]:
        """
        Converts the entire catalog into searchable text.
        """

        return [
            self.build_document(item)
            for item in catalog
        ]

    def generate_embeddings(
        self,
        documents: List[str]
    ) -> np.ndarray:
        """
        Generates normalized embeddings.
        """

        embeddings = self.model.encode(
            documents,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

        return embeddings

    def generate_query_embedding(
        self,
        query: str
    ) -> np.ndarray:
        """
        Generates embedding for user query.
        """

        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype(np.float32)