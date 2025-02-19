import requests
from bs4 import BeautifulSoup
import logging


def fetch_google_news():
    """Fetch Technology news from Google News RSS feed."""
    url_rss = "https://news.google.com/rss/topics/CAAqLAgKIiZDQkFTRmdvSkwyMHZNR1ptZHpWbUVnVjZhQzFVVnhvQ1ZGY29BQVAB?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
    logging.info(f"Fetching news from: {url_rss}")
    response = requests.get(url_rss)
    
    if response.status_code != 200:
        logging.error(f"Failed to fetch news: {response.status_code}")
        return []

    # XML processed by lxml package
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")

    news_list = []
    for item in items:
        title = item.title.text
        link = item.link.text
        published_at = item.pubDate.text
        description = item.description.text if item.description else "No description available"

        news_list.append({
            "title": title,
            "url": link,
            "published_at": published_at,
            "content": description
        })

    logging.info(f"Fetched {len(news_list)} articles from Google News.")
    return news_list

if __name__ == "__main__":
    news = fetch_google_news()
    logging.info(f"Fetched {len(news)} articles from Google News:")
    for article in news:
        logging.info(f"- {article['title']} ({article['url']})")