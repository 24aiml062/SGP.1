# System Architecture

## High-Level Architecture

```
User Browser (Port 8001)
    ↓
Frontend Server (HTML/CSS/JS)
    ↓ HTTP/JSON
Backend Server (Port 8000)
    ↓ FastAPI
Hybrid AI Agent
    ├── OpenAI GPT (AI)
    └── Rule-Based Logic
```

## Component Breakdown

### 1. Frontend (Port 8001)

**Files:**
- `index.html` - Homepage
- `about.html` - About page
- `analyze.html` - Strategy generator
- `style.css` - Design system
- `script.js` - Frontend logic

**Responsibilities:**
- User interface
- Form validation
- API communication
- Results display

**Technology:**
- Pure HTML/CSS/JavaScript
- No build process
- Served by Python HTTP server

### 2. Backend (Port 8000)

**Files:**
- `main.py` - FastAPI application
- `agent.py` - Hybrid AI agent

**Responsibilities:**
- API endpoints
- Data validation
- Strategy generation
- AI orchestration

**Technology:**
- FastAPI framework
- Uvicorn ASGI server
- Pydantic validation

### 3. Hybrid AI Agent

**Components:**

**AI-Powered (OpenAI GPT):**
- Business positioning
- Growth strategies
- Content ideas
- Social media captions
- Hashtag suggestions

**Rule-Based:**
- Platform recommendations
- Action plans
- Local expansion strategies

**Fallback:**
- Automatic fallback to rules if AI unavailable
- No breaking changes
- Graceful degradation

## Request Flow

```
1. User fills form
   ↓
2. JavaScript validates input
   ↓
3. POST /generate-strategy
   ↓
4. FastAPI validates (Pydantic)
   ↓
5. Agent.generate_strategy()
   ├── Check if AI available
   ├── Generate AI content (if available)
   ├── Generate rule-based structure
   └── Merge results
   ↓
6. Return JSON response
   ↓
7. JavaScript displays results
```

## Data Flow

```
Business Input
    ↓
{
  business_name: string
  business_type: string
  products_services: string
  location: string
  target_customers: string
  price_range: string
  current_presence: string
  goals: string
}
    ↓
API Processing
    ↓
Strategy Output
    ↓
{
  business_positioning: {...}
  platform_strategy: {...}
  growth_strategy: {...}
  content_strategy: {...}
  content_ideas: {...}
  sample_content: {...}
  local_expansion: {...}
  action_plan_30_days: {...}
}
```

## Hybrid AI Logic

```python
def generate_strategy(business_data):
    # Rule-based (always)
    platforms = _recommend_platforms()
    action_plan = _generate_action_plan()
    
    # AI-powered (if available)
    if self.use_ai:
        ai_content = _generate_ai_content()
    else:
        ai_content = _generate_template_content()
    
    # Merge
    return {
        "ai_generated": ai_content,
        "rule_based": platforms,
        ...
    }
```

## Scalability Considerations

**Current:**
- Single server
- Synchronous processing
- No caching

**Future Enhancements:**
- Load balancing
- Async processing
- Redis caching
- Database storage
- Rate limiting
