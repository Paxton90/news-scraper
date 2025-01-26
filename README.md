# News Scraper Project

This project is a Python-based application to periodically scrape news articles from an RSS feed and store them in a SQLite database.

## Why This Topic ?

I chose this topic because it demonstrates practical use cases like automating data collection for journalism.
This project showcases essential backend development skills such as scraping, database management, and automation.
It can be used like a TV in a hall or anywhere you can access new information during your free time.

## Dockerization ?

Yes

```cmd
    git clone https://github.com/Paxton90/news-scraper.git
    cd news-scraper
    docker build -t news-scraper .
    docker run -d --name news-scraper-container news-scraper
```

## Possible Extensions ?

- **Docker Multi-stage Build**: When project growing larger, docker Multi-stage build is a good way to reduce docker image size.
- **Multiple Sources**: Automated scraping for multiple RSS feeds by keyword and extract topics from them.
- **User Interface**: Add a front-end dashboard to display the stored news articles. For example: slides can be shown on TV and categories is filtered by what you are intrested.

## Features

1. **Periodic News Scraping**: Fetches news articles from google news technology category RSS feed.
2. **Database Integration**: Stores fetched news articles in a SQLite database (`data/news.db`) and ensures no duplicate entries by uniqueness in url.
3. **Scheduled Tasks**: Automatically fetches news every 5 minutes using the `schedule` library.

## Setup and Usage

### Prerequisites

- Python 3.12
- Install required libraries:

    ```python
        pip install -r requirements.txt
    ```

### Running the Application

1. **Initialize the database**:
 The database will automatically be created at `data/news.db` when the db file is not exist.

2. **Start the scraper**:

    ```python
        python news_scraper/main.py
    ```

3. **Logs**:
The application prints logs to indicate the number of articles fetched and saved during each scraping session.
