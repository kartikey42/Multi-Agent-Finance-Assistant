# Multi-Agent Finance Assistant

This project is a voice-enabled, multi-agent finance assistant that delivers a Morning Market Brief using real-time APIs, scraping agents, FAISS-based retrieval, and LLM-powered synthesis. It responds to the question:

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

---

## 🧠 System Architecture

```
User (Voice Input)
  ↓
STT (Whisper)
  ↓
FastAPI Orchestrator
  ↓
├── API Agent (Yahoo Finance / AlphaVantage)
├── Scraping Agent (Earnings Web Crawler)
├── Retriever Agent (FAISS)
├── Analytics Agent (Risk & Surprise Computation)
├── Language Agent (LLM via LangChain or CrewAI)
↓
TTS (pyttsx3)
↓
Streamlit App
```

---

## 📁 Project Structure

```
multi_agent_finance_assistant/
├── data_ingestion/
│   ├── api_agent.py
│   ├── scraper_agent.py
├── retriever/
│   ├── vector_store.py
├── agents/
│   ├── analytics_agent.py
│   ├── language_agent.py
│   ├── voice_agent.py
├── orchestrator/
│   ├── main.py
├── streamlit_app/
│   ├── app.py
├── requirements.txt
```

---

## 🚀 Running the Project (Without Docker)

### Step 1: Clone & Set Up Environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Step 2: Start Backend (FastAPI)
```bash
uvicorn orchestrator.main:app --reload
```
Visit: http://localhost:8000/brief

### Step 3: Start Frontend (Streamlit)
```bash
streamlit run streamlit_app/app.py
```
Visit: http://localhost:8501

---

## 💡 Features

- 📊 Real-time stock data using Yahoo Finance or AlphaVantage
- 🕸️ Scraping agent using BeautifulSoup
- 🧠 Vector store retrieval with FAISS and SentenceTransformers
- 📈 Earnings surprise analytics
- 🧾 Narrative generation with LLM (OpenAI + LangChain or CrewAI)
- 🗣️ Whisper STT + pyttsx3 TTS
- ⚡ FastAPI microservices & Streamlit UI

---

## 🔐 Environment Variables (Optional)
Create a `.env` file if using APIs like OpenAI:
```env
OPENAI_API_KEY=your-key
ALPHAVANTAGE_API_KEY=your-key
```

---

## 📄 Documentation

- **ai_tool_usage.md** – Log of prompts, tool usage, model configs
- **Architecture Diagram** – Illustrates agent orchestration

---

## 🧪 Evaluation Criteria (for assignment)
- Technical Depth (pipelines, embeddings, analytics)
- Agent Framework Breadth (LangGraph, FAISS, Whisper)
- UX & Performance (voice input/output latency)
- Code Quality (modular structure)
- Documentation & Deployment (Streamlit app)

---

## 🌐 Deployment (Optional)
Deploy the Streamlit app to [Streamlit Cloud](https://streamlit.io/cloud) or use `ngrok` to expose local endpoints.

---

## 🧰 Tools Used

| Component         | Tools                        |
|------------------|------------------------------|
| STT              | Whisper                      |
| TTS              | pyttsx3 / Coqui / gTTS       |
| Retrieval        | FAISS, SentenceTransformers  |
| LLM              | OpenAI API + LangChain       |
| Orchestration    | FastAPI                      |
| UI               | Streamlit                    |
| Scraping         | BeautifulSoup, Requests      |
| Analytics        | Pandas, NumPy                |
