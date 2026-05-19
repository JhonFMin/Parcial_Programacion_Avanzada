import requests

BASE = "https://restcountries.com/v3.1"

def get_country(name: str) -> dict:
    url = f"{BASE}/name/{name}"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.json()[0]