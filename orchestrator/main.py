# -----------------------------
from fastapi import FastAPI
from data_ingestion.api_agent import get_asia_tech_data
from data_ingestion.scraper_agent import scrape_earnings
from agents.analytics_agent import analyze_risk
from agents.language_agent import synthesize_response
from agents.voice_agent import speak

app = FastAPI()

@app.get("/brief")
def generate_brief():
    market_data = get_asia_tech_data()
    earnings = scrape_earnings()
    risk = analyze_risk(market_data)
    response = synthesize_response(risk, earnings)
    speak(response)
    return {"text": response}