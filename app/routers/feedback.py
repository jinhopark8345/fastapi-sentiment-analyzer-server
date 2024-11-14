from typing import Any, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Feedback

router = APIRouter()

@router.post("/submit-feedback/")
async def submit_feedback(user_id: int, content: str, db: Session = Depends(SessionLocal)):
    try:
        new_feedback = Feedback(user_id=user_id, content=content)
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        return {"message": "Feedback submitted successfully.", "feedback_id": new_feedback.id}
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"error": "An error occurred.", "details": str(e)})
    finally:
        db.close()

@router.get("/get-feedback/{user_id}")
async def get_feedback(user_id: int, db: Session = Depends(SessionLocal)):
    feedback_list = db.query(Feedback).filter(Feedback.user_id == user_id).all()
    if not feedback_list:
        return JSONResponse(status_code=404, content={"error": "No feedback found for this user."})
    return feedback_list
