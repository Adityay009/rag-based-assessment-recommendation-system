from app.services.catalog_loader import CatalogLoader


class CatalogAnalyzer:
    """
    Knows which technologies are explicitly supported
    by the SHL catalog.
    """

    def __init__(self):

        loader = CatalogLoader(
            "data/shl_product_catalog_fixed.json"
        )

        self.catalog = loader.load_catalog()

        self.supported_terms = self._extract_terms()

    def _extract_terms(self):

        terms = set()

        for item in self.catalog:

            name = item["name"].lower()

            description = item["description"].lower()

            text = name + " " + description

            for word in text.split():

                word = word.strip("(),.-")

                if len(word) > 2:
                    terms.add(word)

        return terms

    def is_supported(self, term: str) -> bool:

        return term.lower() in self.supported_terms