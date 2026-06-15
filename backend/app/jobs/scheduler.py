import time
from app.services.news_service import fetch_news

def run_scheduler():

    while True:
        print("Running scheduled fetch...")
        fetch_news()

        time.sleep(3600)  # 每小时执行
