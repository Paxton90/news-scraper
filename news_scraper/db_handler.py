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

if __name__ == "__main__":
    initialize_db()