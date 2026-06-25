from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_sentiment

app = FastAPI(
    title="Arabic Sentiment Analysis API",
    description="Real-time Arabic text sentiment analysis using AraBERT",
    version="1.0.0"
)


# --- Request / Response Schemas ---

class TextInput(BaseModel):
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "هذا المنتج رائع جداً وأنصح به الجميع"
            }
        }

class SentimentResponse(BaseModel):
    text: str
    sentiment: str          # positive / negative / neutral
    confidence: float       # 0.0 - 1.0
    scores: dict            # raw scores for all labels


# --- Routes ---

@app.get("/")
def root():
    return {"message": "Arabic Sentiment Analysis API is running ✅"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=SentimentResponse)
def predict(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    result = predict_sentiment(input.text)
    return result
