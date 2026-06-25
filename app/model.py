from transformers import pipeline
import torch

# --- Load Model Once at Startup ---
# CAMeL-Lab AraBERT fine-tuned for sentiment analysis
# Labels: positive, negative, neutral

MODEL_NAME = "CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment"

print(f"Loading model: {MODEL_NAME} ...")

sentiment_pipeline = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME,
    return_all_scores=True,
    device=-1  # CPU only for free tier
)

print("Model loaded successfully ✅")


# --- Label Mapping ---
# CAMeL model uses: positive, negative, neutral
LABEL_MAP = {
    "positive": "positive",
    "negative": "negative",
    "neutral": "neutral"
}


def predict_sentiment(text: str) -> dict:
    results = sentiment_pipeline(text)

    # Handle both list-of-dicts and list-of-lists formats
    if isinstance(results[0], list):
        items = results[0]
    else:
        items = results

    scores = {item["label"]: round(item["score"], 4) for item in items}
    top = max(items, key=lambda x: x["score"])
    sentiment = LABEL_MAP.get(top["label"], top["label"])
    confidence = round(top["score"], 4)

    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence,
        "scores": scores
    }
