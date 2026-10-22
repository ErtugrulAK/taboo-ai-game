# 🛠️ Backend Developer Commands Guide

Quick reference guide for setting up, installing dependencies, and running the FastAPI backend server.

---

## 1. Virtual Environment Setup

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment

- **Windows (cmd):**
  ```bat
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- **Linux / macOS (bash/zsh):**
  ```bash
  source venv/bin/activate
  ```

---

## 2. Dependency Installation

### Install Python Packages
```bash
pip install -r requirements.txt
```

### NLTK Data
`ai_moderator.py` auto-downloads the WordNet corpus on first use. To prefetch manually:
```bash
python -m nltk.downloader wordnet omw-1.4
```

---

## 3. Run Development Server

```bash
python -m uvicorn server:app --reload
```
The FastAPI application will start at `http://127.0.0.1:8000`.
