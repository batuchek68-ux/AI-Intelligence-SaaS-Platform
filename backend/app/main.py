from fastapi import FastAPI
from app.services.news_service import fetch_news
from app.services.trend_service import analyze_trends
from app.services.ai_service import generate_insights
from app.services.dashboard_service import build_dashboard

app = FastAPI(title="Global Intelligence V11 PRO")

@app.get("/api/run")
def run():

    news = fetch_news()
    trends = analyze_trends(news)
    insights = generate_insights(trends)

    dashboard = build_dashboard(news, trends, insights)

    return dashboard
