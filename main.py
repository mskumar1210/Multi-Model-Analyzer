from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import nlp, cv, fusion

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeResponse(BaseModel):
    text_sentiment: str
    text_summary: str
    topic: str
    image_classification: str
    ocr_text: str
    toxicity_score: float
    automated_response: str

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    text: str = Form(...),
    image: UploadFile = File(...)
):
    # NLP tasks
    topic = nlp.topic_classify(text)
    sentiment = nlp.sentiment(text)
    text_summary = nlp.summarize(text)

    # Computer Vision tasks
    image_bytes = await image.read()
    image_classification = cv.classify(image_bytes)
    ocr_text = cv.ocr(image_bytes)
    toxicity_score = max(nlp.toxicity(text), cv.ocr_toxicity(ocr_text))
    face_emotion = cv.face_emotion(image_bytes)

    # Fusion logic for automated response
    automated_response = fusion.generate(
        sentiment=sentiment,
        text=text,
        image_classification=image_classification,
        ocr_text=ocr_text,
        toxicity_score=toxicity_score,
        face_emotion=face_emotion,
    )

    return {
        "text_sentiment": sentiment,
        "text_summary": text_summary,
        "topic": topic,
        "image_classification": image_classification,
        "ocr_text": ocr_text,
        "toxicity_score": toxicity_score,
        "automated_response": automated_response,
    }
