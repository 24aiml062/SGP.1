# AI Integration Setup Guide

## 🤖 Hybrid AI Agent Overview

The system now uses a **hybrid approach**:
- **Rule-Based Logic** - Platform recommendations, action plans, structure
- **AI (LLM)** - Creative content, personalized strategies, intelligent captions

---

## 📦 Installation

### Step 1: Install AI Dependencies

```bash
cd backend
pip install -r requirements-ai.txt
```

This installs:
- `openai` - OpenAI API client for GPT models

### Step 2: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

### Step 3: Set Environment Variable

**Windows (Command Prompt):**
```bash
set OPENAI_API_KEY=sk-your-key-here
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=sk-your-key-here
```

**Permanent Setup (Windows):**
1. Search "Environment Variables" in Windows
2. Click "Environment Variables"
3. Under "User variables", click "New"
4. Variable name: `OPENAI_API_KEY`
5. Variable value: `sk-your-key-here`
6. Click OK

---

## 🚀 Running the AI-Powered Backend

### Option 1: With AI (Recommended)

```bash
# Set API key first
set OPENAI_API_KEY=sk-your-key-here

# Start backend
cd backend
python main.py
```

You should see:
```
✓ Digital Growth Agent initialized with AI (OpenAI GPT)
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Option 2: Without AI (Fallback)

If you don't set the API key, the system automatically falls back to rule-based mode:

```bash
cd backend
python main.py
```

You'll see:
```
⚠️  OPENAI_API_KEY not found in environment
✓ Digital Growth Agent initialized (rule-based mode)
```

The system still works, just without AI-generated content!

---

## 🔄 How the Hybrid System Works

### What Uses AI:
✅ Business positioning (brand personality, value proposition)
✅ Growth strategies (customer attraction, trust building)
✅ Content strategy (posting frequency, content mix)
✅ Content ideas (social posts, video ideas)
✅ Sample captions (promotional, engagement)
✅ Hashtag suggestions

### What Uses Rules:
✅ Platform recommendations (Instagram, Facebook, Google)
✅ Local expansion strategies
✅ 30-day action plan

### Why Hybrid?

**AI is great for:**
- Creative content
- Personalized messaging
- Unique strategies

**Rules are great for:**
- Consistent structure
- Reliable recommendations
- Fast responses

---

## 💰 Cost Information

### OpenAI Pricing (GPT-3.5-turbo)

- **Input:** $0.0005 per 1K tokens (~750 words)
- **Output:** $0.0015 per 1K tokens (~750 words)

**Per Strategy Generation:**
- Input: ~1,000 tokens = $0.0005
- Output: ~1,500 tokens = $0.0023
- **Total: ~$0.003 per strategy** (less than 1 cent!)

**Monthly Estimates:**
- 100 strategies: $0.30
- 1,000 strategies: $3.00
- 10,000 strategies: $30.00

### Free Tier

New OpenAI accounts get **$5 free credit** (good for ~1,600 strategies!)

---

## 🧪 Testing the AI Integration

### Test 1: Check AI Status

```bash
python test_agent.py
```

Look for:
```
✓ Digital Growth Agent initialized with AI (OpenAI GPT)
```

### Test 2: Generate Strategy

```bash
python test_api.py
```

This tests the full API with AI generation.

### Test 3: Compare AI vs Rules

**With AI:**
- More creative captions
- Personalized strategies
- Unique content ideas
- Business-specific recommendations

**Without AI (rules):**
- Template-based captions
- Generic strategies
- Standard content ideas
- Type-based recommendations

---

## 🔧 Configuration Options

### Change AI Model

Edit `backend/agent.py`:

```python
# Line ~150
response = self.client.chat.completions.create(
    model="gpt-3.5-turbo",  # Fast, cheap
    # model="gpt-4",        # Better quality, more expensive
    # model="gpt-4-turbo",  # Best quality, most expensive
    ...
)
```

**Model Comparison:**

| Model | Quality | Speed | Cost/1K tokens |
|-------|---------|-------|----------------|
| gpt-3.5-turbo | Good | Fast | $0.0005 |
| gpt-4 | Excellent | Medium | $0.03 |
| gpt-4-turbo | Best | Fast | $0.01 |

### Adjust Creativity

Edit `backend/agent.py`:

```python
# Line ~155
temperature=0.7,  # 0.0 = consistent, 1.0 = creative
```

- **0.0-0.3** - Consistent, predictable
- **0.4-0.7** - Balanced (recommended)
- **0.8-1.0** - Creative, varied

### Increase Response Length

Edit `backend/agent.py`:

```python
# Line ~156
max_tokens=2000,  # Increase for longer responses
```

---

## 🐛 Troubleshooting

### Error: "Module 'openai' not found"

**Solution:**
```bash
cd backend
pip install openai
```

### Error: "Invalid API key"

**Solution:**
1. Check your API key is correct
2. Verify it starts with `sk-`
3. Make sure environment variable is set:
   ```bash
   echo %OPENAI_API_KEY%  # Windows CMD
   echo $env:OPENAI_API_KEY  # PowerShell
   ```

### Error: "Rate limit exceeded"

**Solution:**
- You've used your free credits
- Add payment method at https://platform.openai.com/account/billing
- Or wait for rate limit to reset

### AI Not Being Used

**Check:**
1. Is `OPENAI_API_KEY` set?
2. Does the key start with `sk-`?
3. Look for this message when starting:
   ```
   ✓ Digital Growth Agent initialized with AI (OpenAI GPT)
   ```

### Slow Response Times

**Normal:**
- AI generation takes 2-5 seconds
- This is expected for LLM calls

**If too slow:**
- Use `gpt-3.5-turbo` instead of `gpt-4`
- Reduce `max_tokens`
- Consider caching common requests

---

## 📊 Monitoring Usage

### Check OpenAI Dashboard

1. Go to https://platform.openai.com/usage
2. View your API usage
3. Monitor costs
4. Set spending limits

### Add Logging

Edit `backend/agent.py` to add logging:

```python
def _generate_ai_content(self, ...):
    print(f"🤖 Generating AI content for: {name}")
    
    response = self.client.chat.completions.create(...)
    
    print(f"✓ AI generation complete")
    print(f"   Tokens used: {response.usage.total_tokens}")
    print(f"   Estimated cost: ${response.usage.total_tokens * 0.000002:.6f}")
```

---

## 🔒 Security Best Practices

### Never Commit API Keys

Add to `.gitignore`:
```
.env
*.key
secrets.txt
```

### Use Environment Variables

**Don't do this:**
```python
api_key = "sk-abc123..."  # ❌ Hardcoded
```

**Do this:**
```python
api_key = os.getenv("OPENAI_API_KEY")  # ✅ Environment variable
```

### Rotate Keys Regularly

1. Create new API key
2. Update environment variable
3. Delete old key from OpenAI dashboard

---

## 🚀 Production Deployment

### Environment Variables

**Heroku:**
```bash
heroku config:set OPENAI_API_KEY=sk-your-key-here
```

**AWS Lambda:**
Add to environment variables in Lambda configuration

**Docker:**
```bash
docker run -e OPENAI_API_KEY=sk-your-key-here ...
```

### Rate Limiting

Consider adding rate limiting to prevent abuse:

```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.post("/generate-strategy")
@limiter.limit("10/minute")  # Max 10 requests per minute
async def generate_strategy(request: Request, business: BusinessInput):
    ...
```

---

## 📈 Performance Optimization

### Caching

Cache common requests to reduce API calls:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def _generate_ai_content_cached(self, business_hash):
    # Generate content
    ...
```

### Async Processing

For high-traffic applications, consider async:

```python
async def _generate_ai_content(self, ...):
    response = await self.client.chat.completions.create(...)
```

---

## 🎯 Summary

**Setup Steps:**
1. ✅ Install: `pip install -r requirements-ai.txt`
2. ✅ Get API key from OpenAI
3. ✅ Set environment variable: `OPENAI_API_KEY`
4. ✅ Start backend: `python main.py`
5. ✅ Test: Visit http://localhost:8001

**Cost:** ~$0.003 per strategy (less than 1 cent!)

**Fallback:** Works without AI if key not set

**Result:** Intelligent, personalized marketing strategies powered by GPT!

---

## 📚 Additional Resources

- OpenAI API Docs: https://platform.openai.com/docs
- Pricing: https://openai.com/pricing
- Best Practices: https://platform.openai.com/docs/guides/production-best-practices
- Rate Limits: https://platform.openai.com/docs/guides/rate-limits

---

Need help? Check the troubleshooting section or create an issue!
