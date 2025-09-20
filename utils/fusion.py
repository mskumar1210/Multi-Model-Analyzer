def generate(
        sentiment: str,
        text: str,
        image_classification: str,
        ocr_text: str,
        toxicity_score: float,
        face_emotion: str,
) -> str:
    # Fusion logic for multimodal response generation
    if toxicity_score >= 0.5:
        return "Warning: Toxic content detected. Please avoid abusive language."

    if sentiment == "Negative" and face_emotion == "Angry":
        return "We’re sorry about your negative experience. We’ll look into it."

    if "love this product" in text.lower() and "product" in image_classification.lower():
        return "Thank you for your positive feedback!"

    return "Thank you for your feedback."
