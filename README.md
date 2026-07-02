# RAG-Based Assessment Recommendation System

AI-powered Retrieval-Augmented Generation (RAG) system that combines semantic retrieval using FAISS, Sentence Transformers, and Google Gemini to recommend the most relevant SHL assessments through conversational interactions.


![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)

## Project Overview

The RAG-Based Assessment Recommendation System is a Retrieval-Augmented Generation (RAG) application designed to assist recruiters in selecting the most suitable SHL assessments through natural language conversations. The system combines semantic search, vector similarity retrieval, and large language models to understand hiring requirements and recommend relevant assessments with concise explanations and direct SHL catalog links.


## Features

- Multi-turn conversational assessment recommendations
- Semantic retrieval using Sentence Transformers and FAISS
- Natural language intent extraction
- Clarification questions for incomplete recruiter queries
- Assessment comparison support
- Recommendation refinement
- Detection of unsupported technologies with closest SHL alternatives
- RESTful API built with FastAPI
- Dockerized deployment
- Interactive API documentation with Swagger
- Conversation-aware routing for recommendation, clarification, comparison, refinement, and confirmation

## System Architecture

```
                User Query
                     │
                     ▼
             Intent Extraction
                     │
                     ▼
          Conversation Router
                     │
                     ▼
            Query Construction
                     │
                     ▼
     Sentence Transformer Embeddings
                     │
                     ▼
              FAISS Vector Search
                     │
                     ▼
        SHL Assessment Retrieval
                     │
                     ▼
        Gemini Recommendation Engine
                     │
                     ▼
             JSON API Response
```

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| LLM | Google Gemini |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Search | FAISS |
| Language | Python 3.10 |
| API Documentation | Swagger / OpenAPI |
| Deployment | Docker |

## Project Structure

```
app/
├── api/
├── models/
├── prompts/
├── services/
├── utils/

data/
vector_db/
tests/

Dockerfile
requirements.txt
README.md
```

## Installation

### Clone the repository

```bash
git clone https://github.com/Adityay009/rag-based-assessment-recommendation-system.git

cd rag-based-assessment-recommendation-system
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=your_api_key
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

Application:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

## Docker

### Build

```bash
docker build -t rag-based-assessment-recommendation-system .
```

### Run

```bash
docker run --env-file .env -p 8000:8000 rag-based-assessment-recommendation-system
```

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

### Assessment Recommendation

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Need a Java backend developer with 4 years of experience"
    }
  ]
}
```

Example Response

```json
{
  "reply": "Based on your requirements...",
  "recommendations": [
    {
      "name": "Java Frameworks (New)",
      "url": "...",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

## Recommendation Workflow

1. User submits a natural language hiring requirement.
2. Intent extraction identifies role, skills, experience, and hiring objective.
3. Semantic query embeddings are generated.
4. FAISS retrieves the most relevant SHL assessments.
5. Gemini generates grounded recommendations using retrieved assessments.
6. API returns conversational recommendations with assessment links.

## Key Design Decisions

- Modular service-oriented architecture for maintainability.
- Retrieval-Augmented Generation to minimize hallucinations.
- FAISS for efficient semantic similarity search.
- Conversation routing to support recommendation, clarification, comparison, refinement, and confirmation.
- Dockerized deployment for portability and reproducibility.

## Future Improvements

- Persistent conversation memory
- Hybrid semantic and metadata ranking
- Personalized recommendation strategies
- Automatic catalog synchronization
- User authentication and session management

## License

This project is provided for educational and demonstration purposes.