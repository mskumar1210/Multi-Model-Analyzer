import random

def classify(image_bytes: bytes) -> str:
    # Generate a random image class for demo
    classes = ["Restaurant/Indoor", "Person", "Product Box", "Outdoors", "Pet", "Object"]
    return random.choice(classes)

def ocr(image_bytes: bytes) -> str:
    # Generate a random "detected" OCR output for demo
    texts = ["Dirty", "Sale!", "Welcome", "Happy", "Caution", "Enjoy", "No Entry", ""]
    return random.choice(texts)

def ocr_toxicity(ocr_text: str) -> float:
    # Simple toxicity: higher for certain words, lower for others
    ocr_lower = ocr_text.lower()
    toxic_words = {"dirty": 0.78, "stupid": 0.9, "idiot": 0.85}
    for word, score in toxic_words.items():
        if word in ocr_lower:
            return score
    return 0.0

def face_emotion(image_bytes: bytes) -> str:
    # Random emotion for demo
    emotions = ["Angry", "Happy", "Neutral", "Surprised", "Sad"]
    return random.choice(emotions)
