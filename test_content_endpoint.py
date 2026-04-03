import sys, os
sys.path.insert(0, 'backend')
from dotenv import load_dotenv
load_dotenv()

import requests

payload = {
    "content_type": "social_media",
    "platform": "Instagram",
    "variants": 1,
    "brief": {
        "product_name": "Sweet Delights Bakery",
        "description": "Custom cakes and pastries baked fresh daily",
        "target_audience": "Families and event planners",
        "tone": "casual",
        "keywords": ["cakes", "fresh", "local"],
        "cta": "Visit us today!"
    }
}

print("Testing POST /api/content/generate ...")
try:
    res = requests.post("http://localhost:8000/api/content/generate", json=payload, timeout=90)
    print("Status:", res.status_code)
    print("Response:", res.text[:500])
except Exception as e:
    print("Error:", e)
