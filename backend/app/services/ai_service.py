def generate_insights(trends):

    results = []

    for word, count in trends:

        if count >= 5:
            level = "HIGH"
        elif count >= 3:
            level = "MEDIUM"
        else:
            level = "LOW"

        results.append({
            "theme": word,
            "signal": level,
            "impact": f"{word} attention detected in global news"
        })

    return results
