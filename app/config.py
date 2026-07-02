from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

CATALOG_JSON = DATA_DIR / "shl_product_catalog_fixed.json"

FAISS_INDEX = VECTOR_DB_DIR / "shl.index"
CATALOG_METADATA = VECTOR_DB_DIR / "catalog.pkl"

# -----------------------------
# Embedding Model
# -----------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -----------------------------
# Retrieval
# -----------------------------

DEFAULT_TOP_K = 10

# Fetch more than needed so metadata filtering has room
MAX_SEARCH_RESULTS = 30