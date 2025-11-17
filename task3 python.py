import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"    # You can change this to any news website
OUTPUT_FILE = "headlines.txt"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        return response.text
    except Exception as e:
        print("Error fetching HTML:", e)
        return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    
    headlines = []

    # Try getting <h2> or <h3> tags – most news sites use these
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if len(text) > 5:
            headlines.append(text)

    return headlines

def save_to_file(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")
    print(f"Saved {len(headlines)} headlines to {OUTPUT_FILE}")

def main():
    print("Fetching headlines...")
    html = fetch_html(URL)

    if html:
        headlines = parse_headlines(html)
        save_to_file(headlines)
    else:
        print("Unable to download page.")

if __name__ == "__main__":
    main()