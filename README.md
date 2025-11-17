# 📰 News Headlines Scraper

A simple Python script that scrapes the latest headlines from any news
website using **Requests** and **BeautifulSoup**.

## 🚀 Features

-   Scrapes headlines from any news website\
-   Uses browser-like headers\
-   Extracts headline tags (`<h1>`, `<h2>`, `<h3>`)\
-   Saves results into `headlines.txt`\
-   Easy to customize

## 📦 Requirements

    pip install requests
    pip install beautifulsoup4

## 💻 How to Run

    python task3.py

## 🧠 How It Works

1.  Fetch HTML using `requests`\
2.  Parse with BeautifulSoup\
3.  Extract `<h1>`, `<h2>`, `<h3>` tags\
4.  Save results to a text file

## 📄 Output Example

    India records major climate milestone
    US announces new economic changes
    Scientists discover new species
    ...

## ⚙️ Configuration

Modify the URL:

    URL = "https://www.bbc.com/news"

## 🛠 Troubleshooting

**No module named bs4** → Run

    pip install beautifulsoup4

**File not created** → Make sure `headlines.txt` is not a folder.
