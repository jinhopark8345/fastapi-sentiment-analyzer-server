import os
from typing import Dict

from fastapi import Depends, FastAPI, Response
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .classifier.model import Model, get_model

# SQLAlchemy setup
DATABASE_URL = (
    "sqlite:///./feedback.db"  # You can switch to PostgreSQL or another DB as needed
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Define Feedback model
class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(Text, nullable=False)


# Create the database table
Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


app = FastAPI()


@app.post("/submit-feedback/")
async def submit_feedback(user_id: int, content: str):
    """Endpoint to submit user feedback."""
    db = SessionLocal()
    try:
        new_feedback = Feedback(user_id=user_id, content=content)
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        return {
            "message": "Feedback submitted successfully.",
            "feedback_id": new_feedback.id,
        }
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500, content={"error": "An error occurred.", "details": str(e)}
        )
    finally:
        db.close()


@app.get("/get-feedback/{user_id}")
async def get_feedback(user_id: int):
    """Endpoint to get feedback for a specific user."""
    db = SessionLocal()
    try:
        feedback_list = db.query(Feedback).filter(Feedback.user_id == user_id).all()
        if not feedback_list:
            return JSONResponse(
                status_code=404, content={"error": "No feedback found for this user."}
            )
        return feedback_list
    finally:
        db.close()


@app.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment=sentiment, confidence=confidence, probabilities=probabilities
    )


@app.get("/export-feedback")
async def export_feedback(file_path="feedback.json"):
    """Endpoint to export the feedback JSON file."""
    if os.path.exists(file_path):
        # Serve the JSON file as a download
        return FileResponse(
            path=file_path, filename="feedback.json", media_type="application/json"
        )
    else:
        # Return a 404 response if the file does not exist
        return JSONResponse(status_code=404, content={"error": "File not found."})
