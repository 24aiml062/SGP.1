"""Test plan → content integration end-to-end."""
import time, requests

BASE = "http://localhost:8000"
time.sleep(3)

# 1. No plan saved yet — plan_used should be False
print("1. Generate without plan...")
res = requests.post(f"{BASE}/api/content/generate", json={
    "content_type": "social_media", "platform": "Instagram", "variants": 1,
    "brief": {"product_name": "Sweet Delights", "description": "Custom cakes",
              "target_audience": "Families", "tone": "casual"}
}, timeout=90)
assert res.status_code == 200, res.text
data = res.json()
assert data["plan_used"] == False, f"Expected plan_used=False, got {data['plan_used']}"
print(f"   plan_used={data['plan_used']} ✓")
print(f"   body: {data['variants'][0]['body'][:80]}")

# 2. Save a growth plan
print("\n2. Save growth plan...")
plan_payload = {
    "niche": "artisan bakery",
    "growth_objective": "increase Instagram followers",
    "target_audience": "young professionals aged 25-35",
    "tone": "witty",
    "platforms": ["Instagram", "Facebook"]
}
res = requests.post(f"{BASE}/api/content/plan", json=plan_payload, timeout=10)
assert res.status_code == 200, res.text
print(f"   Plan saved: {res.json()}")

# 3. Generate with plan — plan_used should be True
print("\n3. Generate with plan active...")
res = requests.post(f"{BASE}/api/content/generate", json={
    "content_type": "social_media", "platform": "Instagram", "variants": 1,
    "brief": {"product_name": "Sweet Delights", "description": "Custom cakes",
              "target_audience": "Families", "tone": "casual"}
}, timeout=90)
assert res.status_code == 200, res.text
data = res.json()
assert data["plan_used"] == True, f"Expected plan_used=True, got {data['plan_used']}"
print(f"   plan_used={data['plan_used']} ✓")
print(f"   body: {data['variants'][0]['body'][:80]}")

# 4. Fetch plan back
print("\n4. Fetch plan...")
res = requests.get(f"{BASE}/api/content/plan", timeout=10)
assert res.status_code == 200
print(f"   Plan: {res.json()}")

print("\n✓ All integration tests passed!")
