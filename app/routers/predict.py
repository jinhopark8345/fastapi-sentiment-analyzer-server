from fastapi import APIRouter, Depends
from app.classifier.model import Model, get_model
from app.schemas.predict import SentimentRequest, SentimentResponse

router = APIRouter()

@router.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)
