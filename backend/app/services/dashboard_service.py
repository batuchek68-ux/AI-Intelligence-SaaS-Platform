def build_dashboard(news, trends, insights):

    return {
        "summary": {
            "total_news": len(news),
            "top_signals": len(insights)
        },
        "keywords": trends,
        "insights": insights,
        "status": "live"
    }
