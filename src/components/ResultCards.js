import React from "react";

const ResultCards = ({ results }) => (
  <div
    style={{
      border: "1px solid #ddd",
      borderRadius: 6,
      padding: 16,
      backgroundColor: "#f9f9f9",
    }}
  >
    <div>
      <strong>Sentiment:</strong> {results.text_sentiment}
    </div>
    <div>
      <strong>Summary:</strong> {results.text_summary}
    </div>
    <div>
      <strong>Topic:</strong> {results.topic}
    </div>
    <div>
      <strong>Image Classification:</strong> {results.image_classification}
    </div>
    <div>
      <strong>OCR Text:</strong> {results.ocr_text}
    </div>
    <div>
      <strong>Toxicity:</strong> {Math.round(results.toxicity_score * 100)}%
    </div>
    <div>
      <strong>Automated Response:</strong> {results.automated_response}
    </div>
  </div>
);

export default ResultCards;
