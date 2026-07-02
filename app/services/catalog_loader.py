import json
from pathlib import Path
from typing import List, Dict


class CatalogLoader:
    """
    Loads and validates the SHL product catalog.
    """

    def __init__(self, catalog_path: str):
        self.catalog_path = Path(catalog_path)

    def load_catalog(self) -> List[Dict]:
        """
        Load catalog JSON into memory.
        """

        if not self.catalog_path.exists():
            raise FileNotFoundError(
                f"Catalog not found: {self.catalog_path}"
            )

        with open(self.catalog_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Catalog JSON should be a list.")

        print(f"✅ Loaded {len(data)} assessments")

        return data