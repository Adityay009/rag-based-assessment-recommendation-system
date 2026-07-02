from app.services.retriever import Retriever


def main():

    retriever = Retriever()

    results = retriever.retrieve(
        "Looking for Java Backend Developer assessment",
        top_k=5,
    )

    print("\nTop Results\n")

    for i, result in enumerate(results, start=1):

        print("-" * 60)

        print(f"{i}. {result['name']}")

        print(f"Score: {result['similarity_score']}")

        print(f"Categories: {result['keys']}")

        print(f"Duration: {result['duration']}")

        print()


if __name__ == "__main__":
    main()