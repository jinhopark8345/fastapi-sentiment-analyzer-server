from fastapi import APIRouter, Depends
from app.classifier.model import get_model
from app.schemas.predict import SentimentRequest, SentimentResponse

router = APIRouter()


@router.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest, model=Depends(get_model)):
    # TODO: need to update this so that it can handle batch requests
    result = model.predict(request.text)[0]
    label, score = result["label"], result["score"]
    return SentimentResponse(label=label, score=score)
