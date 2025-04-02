from fastapi import FastAPI
from app.routes import router  # Importing the router

# Initialize FastAPI app
app = FastAPI(title="Legal Buddy AI", description="AI-powered legal assistant for Indian laws.")

# Include the routes from `routes.py`
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Legal Buddy AI is running!"}
