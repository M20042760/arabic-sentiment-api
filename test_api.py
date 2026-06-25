"""
Quick test script — run this after starting the API locally.
Usage: python test_api.py
"""

import requests

BASE_URL = "http://localhost:8000"

test_cases = [
    "هذا المنتج رائع جداً وأنصح به الجميع",       # positive
    "الخدمة كانت سيئة جداً ولم أكن راضياً أبداً",  # negative
    "المنتج عادي لا هو جيد ولا سيئ",               # neutral
]

print("=" * 50)
print("Arabic Sentiment Analysis API — Test")
print("=" * 50)

for text in test_cases:
    response = requests.post(f"{BASE_URL}/predict", json={"text": text})
    result = response.json()

    print(f"\nText      : {result['text']}")
    print(f"Sentiment : {result['sentiment'].upper()}")
    print(f"Confidence: {result['confidence'] * 100:.1f}%")
    print(f"Scores    : {result['scores']}")
    print("-" * 50)
