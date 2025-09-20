def topic_classify(text: str) -> str:
    text_lower = text.lower()
    if "restaurant" in text_lower:
        return "Food/Restaurant Review"
    elif "news" in text_lower or "breaking" in text_lower:
        return "News"
    elif "review" in text_lower:
        return "Review"
    else:
        return "Comment"

def sentiment(text: str) -> str:
    text_lower = text.lower()
    if "hate" in text_lower or "bad" in text_lower or "terrible" in text_lower:
        return "Negative"
    elif "love" in text_lower or "great" in text_lower or "excellent" in text_lower:
        return "Positive"
    else:
        return "Neutral"

def summarize(text: str) -> str:
    if len(text) > 100:
        return text[:97] + "..."
    return text

def toxicity(text: str) -> float:
    # A simple keyword-based toxicity proxy (demo)
    text_lower = text.lower()
    toxic_words = ["hate", "stupid", "dumb", "idiot"]
    score = 0.0
    for word in toxic_words:
        if word in text_lower:
            score = max(score, 0.8)
    return score
