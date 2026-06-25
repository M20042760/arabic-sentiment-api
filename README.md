# Arabic Sentiment Analysis API 🇦🇪

A production-ready REST API for real-time Arabic text sentiment analysis using AraBERT, built with FastAPI and deployable via Docker.

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=flat-square&logo=fastapi)]()
[![Model](https://img.shields.io/badge/Model-AraBERT-orange?style=flat-square)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&logo=docker)]()

---

## Overview

Sends Arabic text → returns sentiment label + confidence score. Supports Modern Standard Arabic (MSA) and Arabic dialects via CAMeL-Lab's fine-tuned BERT model.

```
POST /predict
{ "text": "هذا المنتج رائع جداً" }

→ { "sentiment": "positive", "confidence": 0.97, "scores": {...} }
```

---

## Project Structure

```
arabic-nlp-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes
│   └── model.py         # Model loading & inference
├── test_api.py          # Local test script
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the API

```bash
uvicorn app.main:app --reload
```

### 3. Test it

```bash
python test_api.py
```

Or open the interactive docs at: **http://localhost:8000/docs**

---

## Run with Docker

```bash
# Build
docker build -t arabic-sentiment-api .

# Run
docker run -p 8000:8000 arabic-sentiment-api
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/health` | Service status |
| POST | `/predict` | Predict sentiment |

### Request

```json
{
  "text": "هذا المنتج رائع جداً وأنصح به الجميع"
}
```

### Response

```json
{
  "text": "هذا المنتج رائع جداً وأنصح به الجميع",
  "sentiment": "positive",
  "confidence": 0.9712,
  "scores": {
    "positive": 0.9712,
    "negative": 0.0181,
    "neutral": 0.0107
  }
}
```

---

## Model

Uses **CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment** from HuggingFace — a BERT model fine-tuned on Arabic dialectal sentiment data covering Gulf, Egyptian, Levantine, and MSA Arabic.

- [Model card on HuggingFace](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment)

---

## Deployment

Deploy free on [Render.com](https://render.com):

1. Push repo to GitHub
2. Connect repo on Render → New Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Done — your API is live 🚀

---

## Contact

**[Your Name]** — [your.email@example.com] · [LinkedIn](https://linkedin.com/in/yourprofile)
