# Arabic Sentiment Analysis API 🇦🇪

A production-ready REST API for real-time Arabic text sentiment analysis using AraBERT, built with FastAPI and containerized with Docker.

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-latest-green?style=flat-square&logo=fastapi)]()
[![Model](https://img.shields.io/badge/Model-AraBERT-orange?style=flat-square)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&logo=docker)]()

---

## 📸 Demo

![API Demo](screenshots/demo.png)

---

## Overview

Sends Arabic text → returns sentiment label + confidence score. Supports Modern Standard Arabic (MSA) and Arabic dialects via CAMeL-Lab's fine-tuned BERT model.

```
POST /predict
{ "text": "هذا المنتج رائع جداً وأنصح به الجميع" }

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
├── screenshots/
│   └── demo.png         # API demo screenshot
├── test_api.py          # Local test script
├── requirements.txt     # All dependencies
├── Dockerfile           # Container configuration
└── README.md
```

---

## Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/M20042760/arabic-sentiment-api.git
cd arabic-sentiment-api
```

### 2. Create and activate conda environment

```bash
conda create -n arabic-nlp python=3.11
conda activate arabic-nlp
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn transformers torch pydantic
```

### 4. Start the API

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open interactive docs

```
http://localhost:8000/docs
```

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
  "confidence": 0.9723,
  "scores": {
    "positive": 0.9723
  }
}
```

---

## Model

Uses **CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment** from HuggingFace — a BERT model fine-tuned on Arabic sentiment data covering Gulf, Egyptian, Levantine, and Modern Standard Arabic.

- [Model card on HuggingFace](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment)

---

## Model Limitations

- Best accuracy on **Modern Standard Arabic (MSA)** — formal written Arabic
- Neutral sentiment is the hardest class to detect accurately
- Gulf and dialectal Arabic may have lower confidence scores

---

## Tech Stack

| Component | Technology |
|---|---|
| Object Detection | AraBERT (CAMeL-Lab) |
| API Framework | FastAPI |
| Containerization | Docker |
| Language | Python 3.11 |

---

## Contact

**[Your Name]** — [your.email@example.com] · [LinkedIn](https://linkedin.com/in/yourprofile) · [GitHub](https://github.com/M20042760)
