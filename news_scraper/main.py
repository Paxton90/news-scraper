import schedule
import time
import logging
from db_handler import initialize_db, save_to_db
from news_fetcher import fetch_google_news


def scheduled_job():
    """Scheduled job to fetch and save news."""
    logging.info("Fetching news...")
    try:
        news_list = fetch_google_news()
        save_to_db(news_list)
    except Exception as e:
        logging.error(f"Error during scheduled job: {e}")

def main():
    """Main function to initialize and run the scheduler."""
    logging.info("Starting news scraper...")
    initialize_db()

    schedule.every(5).minutes.do(scheduled_job)
    # Run immediately
    scheduled_job()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()