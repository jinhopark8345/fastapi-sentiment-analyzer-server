from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    probabilities: dict[str, float]
    sentiment: str
    confidence: float
