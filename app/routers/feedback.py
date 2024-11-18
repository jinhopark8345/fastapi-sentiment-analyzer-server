# feedback.py

from typing import Any, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.models import Feedback
from app.db.session import get_db
from app.schemas.feedback import (
    FeedbackRequest,
    FeedbackResponse,
    FeedbackListResponse,
)  # Import Pydantic models

router = APIRouter()


@router.post("/submit-feedback/", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest, db: Session = Depends(get_db)):
    try:
        # Using request data directly from the Pydantic model
        new_feedback = Feedback(user_id=request.user_id, content=request.content)
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        return FeedbackResponse(
            message="Feedback submitted successfully.", feedback_id=new_feedback.id
        )
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500, content={"error": "An error occurred.", "details": str(e)}
        )
    finally:
        db.close()


@router.get("/get-feedback/{user_id}", response_model=FeedbackListResponse)
async def get_feedback(user_id: int, db: Session = Depends(get_db)):
    feedback_list = db.query(Feedback).filter(Feedback.user_id == user_id).all()

    if not feedback_list:
        return JSONResponse(
            status_code=404, content={"error": "No feedback found for this user."}
        )

    return FeedbackListResponse(
        feedbacks=[
            {
                "id": feedback.id,
                "user_id": feedback.user_id,
                "content": feedback.content,
            }
            for feedback in feedback_list
        ]
    )
