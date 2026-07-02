from pathlib import Path
from typing import Dict, List, Tuple
import pickle

import faiss
import numpy as np


class VectorStore:
    """
    Handles creation, persistence, loading,
    and searching of the FAISS vector index.
    """

    def __init__(
        self,
        index_path: str = "vector_db/shl.index",
        metadata_path: str = "vector_db/catalog.pkl",
    ):
        self.index_path = index_path
        self.metadata_path = metadata_path

        Path("vector_db").mkdir(exist_ok=True)

    def build_index(
        self,
        embeddings: np.ndarray,
    ) -> faiss.Index:

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatIP(dimension)

        index.add(embeddings.astype(np.float32))

        return index

    def save(
        self,
        index: faiss.Index,
        catalog: List[Dict],
    ) -> None:

        faiss.write_index(index, self.index_path)

        with open(self.metadata_path, "wb") as f:
            pickle.dump(catalog, f)

    def load(
        self,
    ) -> Tuple[faiss.Index, List[Dict]]:

        index = faiss.read_index(self.index_path)

        with open(self.metadata_path, "rb") as f:
            catalog = pickle.load(f)

        return index, catalog

    def search(
        self,
        index: faiss.Index,
        query_embedding: np.ndarray,
        top_k: int = 10,
    ):

        scores, indices = index.search(
            query_embedding.reshape(1, -1),
            top_k,
        )

        return scores[0], indices[0]