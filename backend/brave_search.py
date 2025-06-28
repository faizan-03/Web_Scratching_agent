import os
import requests 
from dotenv import load_dotenv

load_dotenv()

BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")

def search_brave(query: str, count: int = 5) -> list:
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {
        "q": query,
        "count": count
    }

    try:
        res = requests.get("https://api.search.brave.com/res/v1/web/search", headers=headers, params=params)
        results = res.json().get("web", {}).get("results", [])
        return [item.get("url") for item in results if item.get("url")]
    except Exception as e:
        print(f"Brave API error: {e}")
        return []
