import feedparser

RSS = [
    "https://rss.cnn.com/rss/edition.rss",
    "https://feeds.bbci.co.uk/news/rss.xml"
]

def fetch_news():
    items = []

    for url in RSS:
        feed = feedparser.parse(url)

        for e in feed.entries[:20]:
            items.append({
                "title": e.get("title", ""),
                "summary": e.get("summary", ""),
                "time": e.get("published", ""),
                "source": url
            })

    return items
