from fastapi import FastAPI

from app.api.chat import router as chat_router

app = FastAPI(
    title="SHL Assessment Recommendation API",
    description="Conversational SHL Assessment Recommendation Assistant",
    version="1.0.0",
)

app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommendation API is running."
    }