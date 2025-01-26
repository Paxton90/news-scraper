import os
import sqlite3


DB_PATH = os.path.join("data", "news.db")

def initialize_db():
    """Initialize the SQLite database table"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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
            saved_news.append(news)  # Save the successfully inserted news
        except sqlite3.IntegrityError:
            # Skip duplicates since url is unique
            skipped_duplicates += 1

    conn.commit()
    conn.close()

    return skipped_duplicates, saved_news

if __name__ == "__main__":
    initialize_db()