# Digital Growth Agent - Complete Documentation

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architecture](#2-architecture)
3. [Installation & Setup](#3-installation--setup)
4. [User Guide](#4-user-guide)
5. [Technical Documentation](#5-technical-documentation)
6. [API Reference](#6-api-reference)
7. [AI Integration](#7-ai-integration)
8. [Frontend Design](#8-frontend-design)
9. [Testing](#9-testing)
10. [Deployment](#10-deployment)
11. [Troubleshooting](#11-troubleshooting)
12. [Contributing](#12-contributing)

---

## 1. Project Overview

### 1.1 What is Digital Growth Agent?

A web-based platform that helps small and local businesses create personalized digital marketing strategies using AI-powered recommendations.

### 1.2 Key Features

- **AI-Powered Content Generatistrategies
- **Platform Recommendations** - Instagram, Facebook, Google Business Profile
- **Content Strategy** - Posting schedules, content mix, optimal times
- **Ready-to-Use Content** - Social media captions with emojis and hashtags
- **30-Day Action Plan** - Step-by-step implementation roadmap
- **Local Growth Strategies** - Community partnerships and referral programs

### 1.3 Target Audience

Small local businesses including:
- Food & Beverage (bakeries, restaurants, cafes)
- Beauty & Wellness (salons, spas, fitness studios)
- Retail (boutiques, gift shops)
- Services (consulting, repa services)
- Creative (photography, design, art studios)
- Education (tutoring, training, workshops)

### 1.4 Technology Stack

**Backend:**
- Python 3.8+
- FastAPI (web framework)
- Uvicorn (ASGI server)
- OpenAI API (GPT-3.5-turbo/GPT-4)
- Pydantic (data validation)

**Frontend:**
- HTML5
- CSS3 (custom design system)
- Vanilla JavaScript (ES6+)
- No frameworks (lightweight, fast)

**Development Tools:**
- Git (version control)
- Batch scripts (Windows automation)
- Python HTTP server (frontend serving)

---

## 2. Architecture

### 2.1 Systrchitecture

```
┌─────────────────────────────────────────────────────┐
│                   User Browser                      │
│              (http://localhost:8001)                │
└────────────────────┬────────────────────────────────┘
                     │
                     │ HTTP Requests
                     │
┌────────────────────▼────────────────────────────────┐
│              Frontend Server                        │
│              (Python HTTP Server)                   │
│              Port: 8001                             │
│                                                     │
│  ├── index.html (Homepage)                         │
│  ├── about.html (About Page)                       │
│  ├── analyze.html (Strategy Generator)             │
│  ├── style.css (Design System)                     │
│  └── script.js (Frontend Logic)                    │
└────────────────────┬────────────────────────────────┘
                     │
 SON)
                     │
┌────────────────────▼────────────────────────────────┐
│              Backend Server                         │
│              (FastAPI + Uvicorn)                    │
│              Port: 8000                             │
│                                                     │
│  ├── main.py (API Endpoints)                       │
│  └── agent.py (Hybrid AI Agent)                    │
│       ├── AI Generation (OpenAI GPT)               │
│       └── Rule-Based Logic                         │
└────────────────────┬────────────────────────────────┘
                     │
                     │ API Calls
                     │
┌────────────────────▼────────────────────────────────┐
│              OpenAI API                             │
│              (GPT-3.5-turbo / GPT-4)               │
│                                                     │
│  Returns: Intelligent marketing strategies          │
└─────────────────────────────────────────────────────┘
```

### 2.2 Request Flow

```
1. User fills form on analyze.html
   ↓
2. JavaScript sends POST to /generate-strategy
   ↓
3. FastAPI validates input (Pydantic)

4. Agent.generate_strategy() called
   ↓
5. Hybrid processing:
   ├── AI: Creative content (OpenAI GPT)
   └── Rules: Structure & recommendations
   ↓
6. JSON response returned
   ↓
7. JavaScript displays results
   ↓
8. User sees personalized strategy
```

### 2.3 Hybrid AI Architecture

**AI-Powered Components:**
- Business positioning
- Growth strategies
- Content ideas
- Social media captions
- Hashtag suggestions

**Rule-Based Components:**
- Platform recommendations
- Action plans
gies
- Content strategy structure

**Fallback Mechanism:**
```python
if self.use_ai:
    content = self._generate_ai_content(...)
else:
    content = self._generate_template_content(...)
```

---

## 3. Installation & Setup

### 3.1 Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Internet connection** (for package installation)
- **OpenAI API key** (optional, for AI features)

### 3.2 Quick Start (Without AI)

```bash
# 1. Install dependencies
install.bat

# 2. Start application
start.bat

# 3. Browser opens automatically to http://localhost:8001
```

### 3.3 AI Setup (Recommended)

```bash
# 1. Install AI dependencies
install_ai.bat

# 2. Get OpenAI API key
# Visit: https://platform.openai.com/api-keys
# Sign up and create a new key

# 3. Set environment variable
set OPENAI_API_KEY=sk-your-key-here

# 4. Test AI integration
python test_ai.py

# 5. Start application
start.bat
```

### 3.4 Manual Installation

**Backend:**
```bash
cd backend
pip install -r requirements-ai.txt
python main.py
```

**Frontend (new terminal):**
```bash
cd frontend
.server 8001
```

**Access:**
- Frontend: http://localhost:8001
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 3.5 Environment les

**Required for AI:**
- `OPENAI_API_KEY` - Your OpenAI API key

**Setting on Windows:**
```bash
# Temporary (current session)
set OPENAI_API_KEY=sk-your-key-here

# Permanent (system-wide)
# 1. Search "Environment Variables"
# 2. Add new user variable
# 3. Name: OPENAI_API_KEY
# 4. Value: sk-your-key-here
```

---

## 4. User Guide

### 4.1 Accessing the Application

1. Start the application using `start.bat`
2. Browser opens to http://localhost:8001/index.html
3. Navigate using the top menu

### 4.2 Homepage

**Features:**
- Value proposition
- Trust indicators (Free, No CC, Fast, For Small Business)
- Feature showcase (6 cards)
- How it works (4 steps)
- Call-to-action buttons

**Actions:**
- Click "Start Free Analysis" → Go to Analyze page
- Click "Learn More" → Go to About page

### 4.3 About Page

**Content:**
- Problem statement
- Solution overview
- Target audience
- Mission statement

**Purpose:**
- Build trust
- Explain value
- Show who it's for

### 4.4 Analyze Page (Strategy Generator)

**Step 1: Fill Business Information**

Required fields:
- Business Name
ness Type
- Products/Services
- Location
- Target Customers
- Price Range
- Business Goals

Optional:
- Current Digital Presence

**Step 2: Generate Strategy**

Click "Generate My Strategy" button

**Step 3: Review Results**

Strategy includes:
1. Business Positioning
2. Platform Recommendations
3. Growth Strategies
4. Content Strategy
5. Content Ideas
6. Sample Captions & Hashtags
7. 30-Day Action Plan

### 4.5 Using Generated Content

**Promotional Captions:**
- Copy and paste to social media
- Customize as needed
- Include provided hashtags

**Hashtags:**
- Click to copy
- Use 8-15 per post
- Mix general and specific

**Action Plan:**
- Follow week by week
- Check off completed tasks
- Adjust based on results

---

