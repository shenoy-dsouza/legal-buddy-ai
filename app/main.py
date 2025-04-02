from fastapi import FastAPI
from app.api.routes import router
from app.services.query_processor import initialize_search


# Initialize FastAPI app
app = FastAPI(
    title="Legal Buddy AI",
    description="AI-powered legal assistant for Indian laws.",
)


# Register startup event manually
def startup_event():
    print("Initializing FAISS and embedding model...")
    initialize_search()


app.add_event_handler("startup", startup_event)


# Include the routes from `routes.py`
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Legal Buddy AI is running!"}
