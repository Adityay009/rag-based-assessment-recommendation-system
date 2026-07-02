from app.services.catalog_loader import CatalogLoader

loader = CatalogLoader(
    "data/shl_product_catalog_fixed.json"
)

catalog = loader.load_catalog()

print("\nFirst assessment:\n")

print(catalog[0]["name"])
print(catalog[0]["duration"])
print(catalog[0]["keys"])