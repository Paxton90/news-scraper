import schedule
import time
from db_handler import initialize_db, save_to_db
from news_fetcher import fetch_google_news

def scheduled_job():
    """Scheduled job to fetch and save news."""
    print("Fetching news...")
    news_list = fetch_google_news()
    skipped_duplicates, saved_news = save_to_db(news_list)
    print(f"Fetched {len(news_list)} news articles.")
    print(f"Skipped {skipped_duplicates} duplicates.")
    print(f"Saved {len(saved_news)} new articles.")

def main():
    """Main function to initialize and run the scheduler."""
    print("Starting news scraper...")
    initialize_db()

    schedule.every(5).minutes.do(scheduled_job)
    # Run immediately
    scheduled_job()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()