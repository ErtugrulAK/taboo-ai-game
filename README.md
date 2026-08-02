# 🤫 AI Taboo Game

An interactive, AI-powered Taboo game built with **React**, **FastAPI**, **Google Gemini API**, and **NLTK Lemmatization**.

In this game, human players describe a secret target word without using forbidden taboo words. The system uses **NLTK-based natural language processing** to moderate descriptions in real-time and leverages **Google Gemini LLM** to attempt to guess the secret target word.

---

## ✨ Features

- 🎯 **Real-time Taboo Moderation:** NLTK lemmatizer checks descriptions for exact words and root variations (nouns & verbs) to prevent forbidden word usage.
- 🤖 **AI-Powered Guesser:** Integrates Google Gemini (`gemini-2.5-flash-lite`) to analyze combined descriptions and provide smart guesses.
- ⚡ **Fast & Responsive UI:** Built with React 19, Vite, and custom modern CSS dark-mode styling.
- ⏱️ **Game Mechanics:** Timer countdown, pass limit handling, real-time score keeping, and game-over state management.
- 🌐 **RESTful Backend API:** Clean FastAPI endpoints for word fetching, validation, and AI guessing.

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** React 19 + Vite
- **Styling:** CSS3 (Custom Dark Mode & Animations)
- **HTTP Client:** Fetch API

### Backend
- **Framework:** FastAPI + Uvicorn
- **AI Model:** Google GenAI SDK (`google-genai` / Gemini API)
- **NLP Engine:** NLTK (`WordNetLemmatizer`)
- **Config & Validation:** `python-dotenv`, Pydantic

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v18+) and **npm**
- **Python** (v3.10+)
- **Google Gemini API Key** ([Get your API key here](https://aistudio.google.com/))

---

### 1. Backend Setup

1. **Navigate to the Backend directory:**
   ```bash
   cd Backend
   ```

2. **Create and activate a Python virtual environment:**
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/Scripts/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file inside the `Backend` directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. **Start the FastAPI Backend Server:**
   ```bash
   python gameStart.py
   # OR
   python -m uvicorn server:app --reload
   ```
   The backend server will run at `http://localhost:8000`.

---

### 2. Frontend Setup

1. **Navigate to the Frontend directory:**
   ```bash
   cd Frontend
   ```

2. **Install Node.js packages:**
   ```bash
   npm install
   ```

3. **Set up Environment Variables:**
   Create a `.env` file inside the `Frontend` directory:
   ```env
   VITE_API_URL=http://localhost:8000
   ```

4. **Start the Vite Frontend Server:**
   ```bash
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 📡 API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `GET /` | `GET` | Health check endpoint |
| `/api/get-word` | `POST` | Fetches a random target word and taboo list |
| `/api/check-description` | `POST` | Validates player description against taboo words via NLTK |
| `/api/guess-word` | `POST` | Sends description to Gemini AI model for guessing |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
