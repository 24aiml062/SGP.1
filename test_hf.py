import sys, os
sys.path.insert(0, 'backend')
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import InferenceClient

key = os.getenv('HF_API_KEY')
client = InferenceClient(api_key=key)

models = [
    "Qwen/Qwen2.5-7B-Instruct",
    "Qwen/Qwen2.5-3B-Instruct",
    "microsoft/Phi-3.5-mini-instruct",
    "google/gemma-2-2b-it",
    "meta-llama/Llama-3.2-3B-Instruct",
]

prompt = 'Return ONLY this JSON, no other text: {"body": "Fresh cakes daily! 🎂", "hashtags": ["#bakery", "#fresh"]}'

for model in models:
    print(f"\nTrying: {model}")
    try:
        result = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You output only valid JSON. No explanation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
        )
        text = result.choices[0].message.content
        print(f"  Response: {text[:120]}")
        import json, re
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            json.loads(match.group())
            print(f"  JSON VALID ✓")
            break
    except Exception as e:
        print(f"  FAIL: {str(e)[:100]}")
