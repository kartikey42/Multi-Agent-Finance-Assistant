# -----------------------------
import requests
from bs4 import BeautifulSoup

def scrape_earnings():
    # Placeholder: Replace with actual news/filings site
    url = "https://example.com/earnings"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # Simulate parsed result
    return {
        "TSMC": {"surprise": "+4%"},
        "Samsung": {"surprise": "-2%"}
    }
