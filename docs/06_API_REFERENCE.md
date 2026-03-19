# API Reference

## Base URL

**Development:** `http://localhost:8000`
**Production:** `https://your-domain.com/api`

## Authentication

Currently no authentication required.

**Future:** API key authentication planned.

## Endpoints

### 1. Health Check

**GET /**

Check if API is running.

**Request:**
```http
GET / HTTP/1.1
Host: localhost:8000
```

**Response:**
```json
{
  "message": "AI Digital Growth Agent API"
}
```

**Status Codes:**
- `200 OK` - API is running

---

### 2. Generate Strategy

**POST /generate-strategy**

Generate personalized digital marketing strategy.

**Request:**
```http
POST /generate-strategy HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "business_name": "Sweet Delights Bakery",
  "business_type": "Bakery",
  "products_services": "Custom cakes, pastries, desserts",
  "location": "Downtown Chicago",
  "target_customers": "Families, event planners",
  "price_range": "Mid-range",
  "current_presence": "Facebook page",
  "goals": "Increase local visibility"
}
```

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| business_name | string | Yes | Name of the business |
| business_type | string | Yes | Type of business (e.g., "Bakery") |
| products_services | string | Yes | Products or services offered |
| location | string | Yes | Business location |
| target_customers | string | Yes | Target customer description |
| price_range | string | Yes | "Budget-friendly", "Mid-range", or "Premium" |
| current_presence | string | No | Current digital presence (default: "None") |
| goals | string | Yes | Business goals |

**Response:**
```json
{
  "business_positioning": {
    "brand_personality": "Warm, creative, and delightful",
    "value_proposition": "Quality custom cakes for families...",
    "ideal_customer": "Families, event planners",
    "tone": "Friendly, authentic, and community-focused"
  },
  "platform_strategy": {
    "recommended_platforms": [
      {
        "platform": "Instagram",
        "priority": 1,
        "reason": "Visual content showcases products effectively"
      },
      {
        "platform": "Google Business Profile",
        "priority": 2,
        "reason": "Essential for local search visibility"
      },
      {
        "platform": "Facebook",
        "priority": 3,
        "reason": "Broad reach and community engagement"
      }
    ],
    "priority_order": ["Instagram", "Google Business Profile", "Facebook"],
    "rationale": "Based on your target audience and business type"
  },
  "growth_strategy": {
    "customer_attraction": [
      "Share behind-the-scenes content",
      "Post customer testimonials and reviews",
      "Run local promotions and special offers",
      "Use location tags and local hashtags"
    ],
    "trust_building": [...],
    "visibility_improvement": [...],
    "retention_tactics": [...]
  },
  "content_strategy": {
    "posting_frequency": {
      "Instagram": "Daily stories, 3-4 feed posts per week",
      "Facebook": "3-5 posts per week",
      "Google Business": "Weekly updates"
    },
    "optimal_times": "Weekdays 9-11 AM, 6-8 PM; Weekends 10 AM-2 PM",
    "content_mix": {
      "Educational": "30% - Tips, how-tos, industry insights",
      "Promotional": "30% - Products, offers, announcements",
      "Engagement": "40% - Questions, polls, user content"
    },
    "monthly_themes": [...]
  },
  "content_ideas": {
    "social_posts": [...],
    "video_ideas": [...],
    "engagement_initiatives": [...]
  },
  "sample_content": {
    "promotional_captions": [
      "✨ Discover quality custom cakes at Sweet Delights! ...",
      "🎉 Special offer this week! ...",
      "💯 Why choose Sweet Delights? ..."
    ],
    "engagement_captions": [...],
    "hashtag_suggestions": [
      "#Bakery",
      "#LocalBusiness",
      "#ShopLocal",
      ...
    ]
  },
  "local_expansion": {
    "community_collaborations": [...],
    "local_partnerships": [...],
    "referral_strategies": [...]
  },
  "action_plan_30_days": {
    "week_1": [...],
    "week_2": [...],
    "week_3": [...],
    "week_4": [...]
  }
}
```

**Status Codes:**
- `200 OK` - Strategy generated successfully
- `400 Bad Request` - Invalid input data
- `422 Unprocessable Entity` - Validation error
- `500 Internal Server Error` - Server error

**Error Response:**
```json
{
  "detail": [
    {
      "loc": ["body", "business_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## Interactive API Documentation

FastAPI provides automatic interactive documentation:

**Swagger UI:** http://localhost:8000/docs
**ReDoc:** http://localhost:8000/redoc

Features:
- Try out endpoints directly
- See request/response schemas
- View validation rules
- Test with sample data

---

## Code Examples

### Python (requests)

```python
import requests

url = "http://localhost:8000/generate-strategy"
data = {
    "business_name": "Sweet Delights Bakery",
    "business_type": "Bakery",
    "products_services": "Custom cakes, pastries",
    "location": "Downtown Chicago",
    "target_customers": "Families",
    "price_range": "Mid-range",
    "goals": "Increase visibility"
}

response = requests.post(url, json=data)
strategy = response.json()

print(strategy["business_positioning"]["brand_personality"])
```

### JavaScript (fetch)

```javascript
const url = 'http://localhost:8000/generate-strategy';
const data = {
    business_name: "Sweet Delights Bakery",
    business_type: "Bakery",
    products_services: "Custom cakes, pastries",
    location: "Downtown Chicago",
    target_customers: "Families",
    price_range: "Mid-range",
    goals: "Increase visibility"
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(strategy => {
    console.log(strategy.business_positioning.brand_personality);
});
```

### cURL

```bash
curl -X POST "http://localhost:8000/generate-strategy" \
  -H "Content-Type: application/json" \
  -d '{
    "business_name": "Sweet Delights Bakery",
    "business_type": "Bakery",
    "products_services": "Custom cakes, pastries",
    "location": "Downtown Chicago",
    "target_customers": "Families",
    "price_range": "Mid-range",
    "goals": "Increase visibility"
  }'
```

---

## Rate Limiting

**Current:** No rate limiting

**Recommended for Production:**
- 10 requests per minute per IP
- 100 requests per hour per IP

**Implementation:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/generate-strategy")
@limiter.limit("10/minute")
async def generate_strategy(...):
    ...
```

---

## CORS Configuration

**Current:** Allows all origins (development)

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # All origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Production:** Restrict to specific domains

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)
```

---

## Response Times

**Rule-Based Mode:**
- Average: 50ms
- Max: 100ms

**AI-Powered Mode:**
- Average: 2-5 seconds
- Max: 10 seconds

**Factors:**
- OpenAI API latency
- Network speed
- Server load

---

## Error Handling

### Validation Errors (422)

```json
{
  "detail": [
    {
      "loc": ["body", "business_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Server Errors (500)

```json
{
  "detail": "Internal server error"
}
```

### AI Errors

If AI generation fails, system automatically falls back to rule-based mode. No error returned to client.

---

## Best Practices

### Request Optimization

1. **Provide Complete Data** - More details = better results
2. **Be Specific** - Clear descriptions improve AI output
3. **Cache Results** - Don't regenerate for same input

### Error Handling

```javascript
try {
    const response = await fetch(url, options);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
} catch (error) {
    console.error('Error:', error);
    // Handle error appropriately
}
```

### Timeout Handling

```javascript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 10000); // 10s timeout

fetch(url, {
    ...options,
    signal: controller.signal
})
.then(response => {
    clearTimeout(timeoutId);
    return response.json();
})
.catch(error => {
    if (error.name === 'AbortError') {
        console.log('Request timed out');
    }
});
```

---

## Versioning

**Current:** v1 (no version in URL)

**Future:** Version in URL path
- `/v1/generate-strategy`
- `/v2/generate-strategy`

---

## Changelog

### v2.0 (Current)
- Added AI-powered content generation
- Improved response quality
- Added graceful fallback

### v1.0
- Initial release
- Rule-based generation only
