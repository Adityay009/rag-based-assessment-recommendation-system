from app.models.request_models import ChatRequest
from app.services.recommender import RecommenderService


def main():

    recommender = RecommenderService()

    request = ChatRequest(
        message="Looking for a Java backend developer with 4 years experience"
    )

    response = recommender.recommend(request)

    print("\n")
    print("=" * 80)
    print(response.response)
    print("=" * 80)

    print("\nRecommendations\n")

    for assessment in response.recommendations:

        print(
            assessment.name,
            "|",
            assessment.similarity_score,
        )


if __name__ == "__main__":
    main()