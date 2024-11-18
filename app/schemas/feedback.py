from pydantic import BaseModel
from typing import List


class FeedbackRequest(BaseModel):
    user_id: int  # The ID of the user submitting feedback
    content: str  # The content of the feedback


class FeedbackResponse(BaseModel):
    message: str  # Message indicating success or failure
    feedback_id: int  # The ID of the submitted feedback (optional for success response)


class FeedbackItem(BaseModel):
    id: int
    user_id: int
    content: str


class FeedbackListResponse(BaseModel):
    feedbacks: List[FeedbackItem]
