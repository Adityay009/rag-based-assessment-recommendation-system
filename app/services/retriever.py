from typing import Dict, List, Optional

import numpy as np

from app.config import DEFAULT_TOP_K, MAX_SEARCH_RESULTS
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class Retriever:
    """
    Performs semantic retrieval over the SHL catalog using FAISS.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

        self.index, self.catalog = self.vector_store.load()

    def retrieve(
        self,
        query: str,
        filters: Optional[Dict] = None,
        top_k: int = DEFAULT_TOP_K,
    ) -> List[Dict]:

        query_embedding = self.embedding_service.generate_query_embedding(query)

        scores, indices = self.vector_store.search(
            self.index,
            query_embedding,
            top_k=MAX_SEARCH_RESULTS,
        )

        results = []

        for score, idx in zip(scores, indices):

            if idx == -1:
                continue

            assessment = self.catalog[idx].copy()

            assessment["similarity_score"] = round(float(score), 4)

            results.append(assessment)

        if filters:
            results = self._apply_metadata_filters(
                results,
                filters,
            )

        return results[:top_k]

    def _apply_metadata_filters(
        self,
        results: List[Dict],
        filters: Dict,
    ) -> List[Dict]:

        filtered = []

        for assessment in results:

            keep = True

            for key, value in filters.items():

                if key not in assessment:
                    continue

                item_value = assessment[key]

                if isinstance(item_value, list):

                    values = [str(v).lower() for v in item_value]

                    if str(value).lower() not in values:
                        keep = False
                        break

                else:

                    if str(item_value).lower() != str(value).lower():
                        keep = False
                        break

            if keep:
                filtered.append(assessment)

        return filtered