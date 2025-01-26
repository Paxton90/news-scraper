import os
import sqlite3
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("news_scraper.log")
    ]
)

DB_PATH = os.path.join("data", "news.db")

def initialize_db():
    """Initialize the SQLite database table."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                url TEXT NOT NULL UNIQUE,
                published_at TEXT
            )
        ''')
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization error: {e}")
    finally:
        conn.close()

def save_to_db(news_list):
    """Save the news data into the SQLite database and count duplicates."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    skipped_duplicates = 0
    saved_news = []

    for news in news_list:
        try:
            cursor.execute('''
                INSERT INTO news (title, content, url, published_at)
                VALUES (?, ?, ?, ?)
            ''', (news["title"], news["content"], news["url"], news["published_at"]))
            saved_news.append(news)
        except sqlite3.IntegrityError:
            # Skip duplicates since url is unique
            skipped_duplicates += 1
            logging.debug(f"Duplicate found for URL: {news['url']}")

    conn.commit()
    conn.close()

    logging.info(f"Saved {len(saved_news)} new articles. Skipped {skipped_duplicates} duplicates.")
    return skipped_duplicates, saved_news

if __name__ == "__main__":
    initialize_db()