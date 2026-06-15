from fastapi import FastAPI
from app.services.news_service import fetch_news
from app.services.trend_service import analyze_trends
from app.services.ai_service import generate_insights

app = FastAPI(title="Global Intelligence V11")

@app.get("/")
def home():
    return {"status": "ok", "version": "v11"}

@app.get("/run")
def run_pipeline():

    news = fetch_news()
    trends = analyze_trends(news)
    insights = generate_insights(trends)

    return {
        "news_count": len(news),
        "trends": trends,
        "insights": insights
    }
