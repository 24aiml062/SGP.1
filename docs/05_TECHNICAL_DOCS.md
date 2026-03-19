# Technical Documentation

## Backend Architecture

### File Structure

```
backend/
├── main.py                 # FastAPI application
├── agent.py                # Hybrid AI agent
├── requirements-lite.txt   # Basic dependencies
└── requirements-ai.txt     # AI dependencies
```

### main.py - FastAPI Application

**Purpose:** API server that handles HTTP requests

**Key Components:**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import DigitalGrowthAgent

app = FastAPI(title="AI Digital Growth Agent")

# CORS middleware for frontend communication
app.add_middleware(CORSMiddleware, ...)

# Initialize agent once
agent = DigitalGrowthAgent()

# Input validation model
class BusinessInput(BaseModel):
    business_name: str
    business_type: str
    # ... other fields

# API endpoints
@app.get("/")
def root():
    return {"message": "AI Digital Growth Agent API"}

@app.post("/generate-strategy")
async def generate_strategy(business: BusinessInput):
    strategy = agent.generate_strategy(business.dict())
    return strategy
```

**Endpoints:**

1. **GET /**
   - Health check
   - Returns: `{"message": "..."}`

2. **POST /generate-strategy**
   - Generates marketing strategy
   - Input: BusinessInput model
   - Returns: Complete strategy JSON

### agent.py - Hybrid AI Agent

**Purpose:** Generates marketing strategies using AI + rules

**Class Structure:**

```python
class DigitalGrowthAgent:
    def __init__(self):
        # Initialize OpenAI client
        self.client = OpenAI(api_key=...)
        self.use_ai = True/False
    
    def generate_strategy(self, business_data):
        # Main entry point
        # Returns complete strategy
    
    def _generate_ai_content(self, ...):
        # AI-powered content generation
        # Calls OpenAI API
    
    def _generate_platform_strategy(self, ...):
        # Rule-based platform recommendations
    
    # ... other helper methods
```

**AI Integration:**

```python
def _generate_ai_content(self, name, biz_type, ...):
    # Construct prompt
    prompt = f"""You are an expert digital marketing strategist...
    
    Business Name: {name}
    Business Type: {biz_type}
    ...
    
    Generate strategy in JSON format..."""
    
    # Call OpenAI API
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "..."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000,
        response_format={"type": "json_object"}
    )
    
    # Parse and return
    return json.loads(response.choices[0].message.content)
```

**Rule-Based Logic:**

```python
def _recommend_platforms(self, biz_type, target):
    visual_businesses = ["bakery", "salon", "restaurant", ...]
    
    platforms = []
    
    if any(v in biz_type.lower() for v in visual_businesses):
        platforms.append({
            "platform": "Instagram",
            "priority": 1,
            "reason": "Visual content showcases products"
        })
    
    platforms.extend([
        {"platform": "Google Business Profile", ...},
        {"platform": "Facebook", ...}
    ])
    
    return platforms
```

## Frontend Architecture

### File Structure

```
frontend/
├── index.html      # Homepage
├── about.html      # About page
├── analyze.html    # Strategy generator
├── style.css       # Design system
└── script.js       # Frontend logic
```

### Design System (style.css)

**CSS Variables:**

```css
:root {
    /* Colors */
    --primary-blue: #1a56db;
    --teal: #0d9488;
    --orange: #f97316;
    
    /* Spacing */
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    
    /* Typography */
    --font-sans: -apple-system, BlinkMacSystemFont, ...;
    --font-size-base: 1rem;
}
```

**Component Classes:**

- `.btn` - Button base
- `.btn-primary` - Primary action button
- `.card` - Content card
- `.form-group` - Form field container
- `.strategy-section` - Strategy output section

### Frontend Logic (script.js)

**Key Functions:**

```javascript
// Form submission
document.getElementById('businessForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const businessData = {
        business_name: document.getElementById('businessName').value,
        // ... other fields
    };
    
    document.getElementById('loading').style.display = 'flex';
    
    const response = await fetch('http://localhost:8000/generate-strategy', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(businessData)
    });
    
    const strategy = await response.json();
    displayStrategy(strategy);
});

// Display results
function displayStrategy(strategy) {
    let html = '';
    
    // Business Positioning
    html += createSection('Business Positioning', ...);
    
    // Platform Strategy
    html += createSection('Recommended Platforms', ...);
    
    // ... other sections
    
    document.getElementById('strategyOutput').innerHTML = html;
}
```

## Data Models

### Input Model (BusinessInput)

```python
class BusinessInput(BaseModel):
    business_name: str          # Required
    business_type: str          # Required
    products_services: str      # Required
    location: str               # Required
    target_customers: str       # Required
    price_range: str            # Required
    current_presence: str = "None"  # Optional
    goals: str                  # Required
```

### Output Model (Strategy)

```json
{
  "business_positioning": {
    "brand_personality": "string",
    "value_proposition": "string",
    "ideal_customer": "string",
    "tone": "string"
  },
  "platform_strategy": {
    "recommended_platforms": [
      {
        "platform": "string",
        "priority": number,
        "reason": "string"
      }
    ],
    "priority_order": ["string"],
    "rationale": "string"
  },
  "growth_strategy": {
    "customer_attraction": ["string"],
    "trust_building": ["string"],
    "visibility_improvement": ["string"],
    "retention_tactics": ["string"]
  },
  "content_strategy": {
    "posting_frequency": {},
    "optimal_times": "string",
    "content_mix": {},
    "monthly_themes": ["string"]
  },
  "content_ideas": {
    "social_posts": ["string"],
    "video_ideas": ["string"],
    "engagement_initiatives": ["string"]
  },
  "sample_content": {
    "promotional_captions": ["string"],
    "engagement_captions": ["string"],
    "hashtag_suggestions": ["string"]
  },
  "local_expansion": {
    "community_collaborations": ["string"],
    "local_partnerships": ["string"],
    "referral_strategies": ["string"]
  },
  "action_plan_30_days": {
    "week_1": ["string"],
    "week_2": ["string"],
    "week_3": ["string"],
    "week_4": ["string"]
  }
}
```

## Error Handling

### Backend Errors

```python
try:
    ai_content = self._generate_ai_content(...)
except Exception as e:
    print(f"AI generation failed: {e}")
    # Fall back to rule-based
    ai_content = self._generate_template_content(...)
```

### Frontend Errors

```javascript
try {
    const response = await fetch(...);
    if (!response.ok) throw new Error('Failed to generate strategy');
    const strategy = await response.json();
    displayStrategy(strategy);
} catch (error) {
    alert('Error generating strategy. Please ensure backend is running.');
    console.error(error);
}
```

## Performance Considerations

### Response Time

- **Rule-based:** ~50ms
- **AI-powered:** 2-5 seconds
- **Bottleneck:** OpenAI API call

### Optimization Strategies

1. **Caching** - Cache common business types
2. **Async Processing** - Use async/await
3. **Rate Limiting** - Prevent abuse
4. **CDN** - Serve static files from CDN

### Cost Optimization

- Use `gpt-3.5-turbo` (cheaper than GPT-4)
- Set reasonable `max_tokens` limit
- Implement caching for repeated requests
- Monitor usage on OpenAI dashboard

## Security

### API Key Protection

```python
# ✅ Good - Environment variable
api_key = os.getenv("OPENAI_API_KEY")

# ❌ Bad - Hardcoded
api_key = "sk-abc123..."
```

### CORS Configuration

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development
    # allow_origins=["https://yourdomain.com"],  # Production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Input Validation

```python
class BusinessInput(BaseModel):
    business_name: str  # Pydantic validates automatically
    # ... other fields
```

## Testing

### Unit Tests

```python
def test_agent_initialization():
    agent = DigitalGrowthAgent()
    assert agent is not None

def test_strategy_generation():
    agent = DigitalGrowthAgent()
    strategy = agent.generate_strategy(test_data)
    assert "business_positioning" in strategy
```

### Integration Tests

```python
def test_api_endpoint():
    response = client.post("/generate-strategy", json=test_data)
    assert response.status_code == 200
    assert "platform_strategy" in response.json()
```

### Manual Testing

```bash
# Test agent
python test_agent.py

# Test AI integration
python test_ai.py

# Test API
python test_api.py
```

## Deployment

### Environment Variables

```bash
# Production
export OPENAI_API_KEY=sk-your-key-here
export ENVIRONMENT=production
```

### Docker Deployment

```dockerfile
FROM python:3.9
WORKDIR /app
COPY backend/ .
RUN pip install -r requirements-ai.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Cloud Deployment

**Heroku:**
```bash
heroku config:set OPENAI_API_KEY=sk-your-key-here
git push heroku main
```

**AWS Lambda:**
- Use Mangum adapter for FastAPI
- Set environment variables in Lambda configuration
