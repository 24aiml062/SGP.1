# Installation & Setup Guide

## Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Internet connection** (for package installation)
- **OpenAI API key** (optional, for AI features)

## Quick Start (Without AI)

```bash
# 1. Install dependencies
install.bat

# 2. Start application
start.bat

# 3. Browser opens automatically to http://localhost:8001
```

## AI Setup (Recommended)

### Step 1: Install AI Dependencies

```bash
install_ai.bat
```

This installs:
- fastapi
- uvicorn
- pydantic
- python-multipart
- openai

### Step 2: Get OpenAI API Key

1. Visit https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### Step 3: Set Environment Variable

**Windows (Command Prompt):**
```bash
set OPENAI_API_KEY=sk-your-key-here
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

**Permanent Setup (Windows):**
1. Search "Environment Variables" in Windows
2. Click "Environment Variables"
3. Under "User variables", click "New"
4. Variable name: `OPENAI_API_KEY`
5. Variable value: `sk-your-key-here`
6. Click OK

### Step 4: Test AI Integration

```bash
python test_ai.py
```

Expected output:
```
[OK] OpenAI library installed
[OK] OPENAI_API_KEY environment variable is set
[OK] Agent initialized successfully
    Mode: AI-powered (OpenAI GPT)
✓ AI integration is working!
```

### Step 5: Start Application

```bash
start.bat
```

## Manual Installation

### Backend Setup

```bash
cd backend
pip install -r requirements-ai.txt
python main.py
```

You should see:
```
✓ Digital Growth Agent initialized with AI (OpenAI GPT)
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Frontend Setup (New Terminal)

```bash
cd frontend
python -m http.server 8001
```

You should see:
```
Serving HTTP on :: port 8001 (http://[::]:8001/) ...
```

### Access Application

- **Frontend:** http://localhost:8001
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## Verification

### Check Backend

Visit: http://localhost:8000

Should show:
```json
{"message":"AI Digital Growth Agent API"}
```

### Check Frontend

Visit: http://localhost:8001/index.html

Should show the homepage

### Test Strategy Generation

1. Go to http://localhost:8001/analyze.html
2. Fill in business information
3. Click "Generate My Strategy"
4. Wait 2-5 seconds
5. View personalized strategy

## Troubleshooting Installation

### Python Not Found

**Error:** `'python' is not recognized`

**Solution:**
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart terminal

### pip Not Found

**Error:** `'pip' is not recognized`

**Solution:**
```bash
python -m ensurepip --upgrade
```

### Module Not Found

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
cd backend
pip install -r requirements-ai.txt
```

### Port Already in Use

**Error:** `Address already in use`

**Solution:**
- Close other applications using ports 8000 or 8001
- Or change ports in scripts

### OpenAI Not Installed

**Error:** `Module 'openai' not found`

**Solution:**
```bash
pip install openai
```

### Invalid API Key

**Error:** `Invalid API key`

**Solution:**
1. Check your API key is correct
2. Verify it starts with `sk-`
3. Make sure environment variable is set:
   ```bash
   echo %OPENAI_API_KEY%
   ```

## Next Steps

After installation:
1. Read [User Guide](04_USER_GUIDE.md)
2. Explore [API Reference](06_API_REFERENCE.md)
3. Check [AI Integration](07_AI_INTEGRATION.md)
