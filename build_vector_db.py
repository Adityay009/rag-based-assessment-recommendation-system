from app.services.catalog_loader import CatalogLoader
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


def main():

    print("=" * 60)
    print("Building SHL Vector Database")
    print("=" * 60)

    loader = CatalogLoader("data/shl_product_catalog_fixed.json")
    catalog = loader.load_catalog()

    embedding_service = EmbeddingService()

    documents = embedding_service.build_documents(catalog)

    print(f"\nCreated {len(documents)} searchable documents.\n")

    embeddings = embedding_service.generate_embeddings(documents)

    print(f"\nEmbedding Shape: {embeddings.shape}")

    vector_store = VectorStore()

    index = vector_store.build_index(embeddings)

    vector_store.save(index, catalog)

    print("\n✅ Vector database created successfully!")
    print("Index saved to vector_db/shl.index")
    print("Metadata saved to vector_db/catalog.pkl")


if __name__ == "__main__":
    main()