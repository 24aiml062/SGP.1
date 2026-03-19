# AI Digital Growth Agent - Project Documentation

## Project Overview

The **AI Digital Growth Agent** is a web-based application designed to help small businesses create personalized digital marketing strategies. The system analyzes business information and generates comprehensive, actionable marketing recommendations tailored to the specific needs of each business.

---

## Problem Statement

**Challenge:** Small businesses lack access to affordable, professional digital marketing strategy services. Many entrepreneurs struggle to create effective online presence and marketing plans due to limited resources, time, and marketing expertise.

**Solution:** An automated AI-powered agent that:
- Analyzes business information (type, products, target customers, goals)
- Generates comprehensive digital marketing strategies
- Provides platform recommendations and content ideas
- Creates actionable 30-day implementation plans
- Is accessible and user-friendly for non-technical users

---

## Key Features

### 1. **Automated Strategy Generation**
   - Business positioning and brand personality
   - Platform-specific social media strategies
   - Growth tactics tailored to business type
   - Content strategy and ideas
   - Sample content creation
   - Local expansion recommendations
   - 30-day action plans

### 2. **Business-Specific Recommendations**
   - Analyzes business type, products/services, target customers
   - Considers location and pricing strategy
   - Assesses current digital presence
   - Aligns recommendations with business goals

### 3. **User-Friendly Interface**
   - Web-based frontend (no installation needed)
   - Simple form-based input
   - Real-time strategy generation
   - Clear, organized output

---

## Technology Stack

### Backend
- **Framework:** FastAPI (Python)
- **Server:** Uvicorn
- **Core Logic:** DigitalGrowthAgent (Rule-based AI system)
- **API Type:** RESTful JSON API
- **Port:** 8000

### Frontend
- **HTML5** - Page structure
- **CSS3** - Styling
- **JavaScript** - Client-side logic and API communication
- **Server:** HTTP Server (Python's http.server)
- **Port:** 8001

### Dependencies
```
fastapi==0.109.0
uvicorn==0.27.0
pydantic==2.5.3
transformers==4.36.2
torch==2.1.2
python-multipart==0.0.6
```

---

## Project Structure

```
sgp2/
├── backend/
│   ├── agent.py              # DigitalGrowthAgent class (core logic)
│   ├── main.py              # FastAPI application
│   ├── requirements.txt      # Python dependencies
│   └── requirements-lite.txt # Minimal dependencies
│
├── frontend/
│   ├── index.html           # Main application page
│   ├── about.html           # About page
│   ├── analyze.html         # Analysis/results page
│   ├── script.js            # Frontend logic
│   └── style.css            # Styling
│
├── install.bat              # Automated installation script
├── start.bat                # Automated startup script
├── run_backend.bat          # Backend runner
├── run_frontend.bat         # Frontend runner
├── setup.bat                # Full setup script
├── setup_lite.bat           # Lightweight setup
├── check_setup.bat          # Verification script
│
├── test_agent.py            # Agent functionality tests
├── test_api.py              # API endpoint tests
├── test_pages.py            # Frontend page tests
│
├── HOW_TO_RUN.txt           # User instructions
└── DOCUMENTATION.md         # This file
```

---

## Data Flow

### User Input
Users provide the following business information through the web form:
- Business name
- Business type (e.g., e-commerce, service-based, retail)
- Products/services offered
- Location
- Target customer profile
- Price range
- Current digital presence
- Marketing goals

### Processing
1. Frontend sends POST request to `/generate-strategy` endpoint
2. Backend DigitalGrowthAgent analyzes the input
3. Agent generates strategy components:
   - Business positioning
   - Platform recommendations
   - Growth strategies
   - Content strategies and ideas
   - Sample content
   - Local expansion plans
   - 30-day action plan

### Output
Users receive a comprehensive strategy including:
- Brand positioning and personality
- Platform strategy (which social media to use)
- Growth tactics and opportunities
- Content calendar ideas
- Sample posts and content
- Local expansion strategies
- Detailed 30-day action plan

---

## API Endpoints

### GET `/`
- **Purpose:** Health check
- **Response:** `{"message": "AI Digital Growth Agent API"}`

### POST `/generate-strategy`
- **Purpose:** Generate marketing strategy
- **Request Body:**
  ```json
  {
    "business_name": "string",
    "business_type": "string",
    "products_services": "string",
    "location": "string",
    "target_customers": "string",
    "price_range": "string",
    "current_presence": "string (optional)",
    "goals": "string"
  }
  ```
- **Response:** Strategy object with all components
- **Port:** 8000

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Windows (or similar OS with batch file support)

### Quick Start (Windows)
```bash
# Step 1: Install dependencies
double-click install.bat

# Step 2: Start the application
double-click start.bat

# Step 3: Open browser and navigate to http://localhost:8001
```

### Manual Setup
```bash
# Terminal 1: Backend
cd backend
python main.py
# Backend runs on http://0.0.0.0:8000

# Terminal 2: Frontend
cd frontend
python -m http.server 8001
# Frontend available at http://localhost:8001
```

---

## Usage Guide

### For End Users
1. **Open Application:** Go to `http://localhost:8001` in your web browser
2. **Fill Form:** Enter your business information in the input form
3. **Generate Strategy:** Click "Generate Strategy" button
4. **View Results:** Wait 2-3 seconds for the strategy to generate
5. **Review & Implement:** Study the recommendations and follow the 30-day action plan

### For Developers

#### Running Tests
```bash
# Test the agent logic
python test_agent.py

# Test API endpoints
python test_api.py

# Test frontend pages
python test_pages.py
```

#### Checking System Setup
```bash
# Verify all dependencies are installed
check_setup.bat
```

---

## Core Components

### DigitalGrowthAgent (`agent.py`)
The intelligent core that generates strategies:

**Main Method:**
- `generate_strategy(business_data)` - Takes business information and returns complete marketing strategy

**Sub-generation Methods:**
- `_generate_positioning()` - Brand positioning
- `_generate_platform_strategy()` - Social media platform recommendations
- `_generate_growth_strategy()` - Growth tactics
- `_generate_content_strategy()` - Content planning
- `_generate_content_ideas()` - Content inspiration
- `_generate_sample_content()` - Ready-to-use content
- `_generate_local_expansion()` - Local market strategies
- `_generate_action_plan()` - 30-day implementation plan

**Helper Methods:**
- `_get_brand_personality()` - Determine brand tone and personality
- `_recommend_platforms()` - Select best social media platforms
- Other utility methods for data processing

### FastAPI Backend (`main.py`)
- Provides REST API interface
- Handles CORS for cross-origin requests
- Routes requests to the DigitalGrowthAgent
- Validates input using Pydantic models

### Frontend (`index.html`, `script.js`, `style.css`)
- Responsive web interface
- Form validation and submission
- Real-time API communication
- Result display and formatting

---

## Troubleshooting

### Problem: "Python is not recognized"
**Solution:** 
- Install Python from https://www.python.org/
- During installation, check "Add Python to PATH"
- Restart your computer

### Problem: Port Already in Use
**Solution:**
- Close other programs using ports 8000 or 8001
- Or restart your computer
- Or modify the port in `main.py` and `script.js`

### Problem: "Failed to generate strategy"
**Solution:**
- Ensure both backend and frontend are running
- Check backend window for "Uvicorn running on http://0.0.0.0:8000"
- Check browser console for errors (F12)

### Problem: Dependencies Not Installing
**Solution:**
- Run `setup_lite.bat` for minimal installation
- Or manually run: `pip install -r requirements.txt`
- Ensure pip is up to date: `pip install --upgrade pip`

---

## Future Enhancements

Potential improvements and features:
- [ ] Integration with actual AI models (GPT, Transformers)
- [ ] Database storage for saved strategies
- [ ] Strategy export (PDF, Word)
- [ ] Analytics dashboard
- [ ] Email notification system
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] AI-generated images for content
- [ ] Integration with social media APIs
- [ ] Performance tracking and metrics

---

## Performance Specifications

- **Strategy Generation Time:** 2-3 seconds
- **Recommended Browsers:** Chrome, Firefox, Safari, Edge
- **Backend Concurrency:** Supports multiple simultaneous requests
- **Data Size:** Strategies typically 10-50KB JSON objects
- **Memory Usage:** < 500MB for typical operation

---

## Security Considerations

Current implementation:
- No sensitive data storage
- CORS enabled for development
- No authentication/authorization (development stage)
- Input validation via Pydantic

Recommendations for production:
- Implement authentication/user accounts
- Add rate limiting
- Sanitize user inputs
- Use HTTPS/SSL
- Implement logging and monitoring
- Add database security measures

---

## Support & Maintenance

### Checking System Health
Run `check_setup.bat` to verify:
- Python installation
- All required packages
- Port availability
- Configuration validity

### Logs & Debugging
- Backend logs appear in the backend command window
- Frontend errors visible in browser console (F12)
- Test files for verification: `test_agent.py`, `test_api.py`, `test_pages.py`

### Getting Help
1. Check `HOW_TO_RUN.txt` for quick start
2. Look for error messages in logs
3. Run diagnostics with `check_setup.bat`
4. Review this documentation

---

## Version Information

- **Project Version:** 1.0
- **Created:** 2026
- **Status:** Development
- **Python Version Requirement:** 3.8+

---

## Conclusion

The AI Digital Growth Agent provides an innovative, accessible solution for small businesses seeking professional digital marketing guidance. By combining rule-based AI logic with a user-friendly interface, it democratizes access to marketing strategy expertise.

The modular architecture allows for easy expansion, enabling future integration with advanced AI models, analytics, and third-party services.

---

**Last Updated:** February 18, 2026
