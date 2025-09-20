import React, { useState } from "react";

const UploadBox = ({ setResults }) => {
  const [text, setText] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!text || !image) {
      setError("Please enter text and select an image.");
      return;
    }
    setError(null);
    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("text", text);
      formData.append("image", image);

      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to fetch analysis");
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
      setResults(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text here"
        style={{ width: "100%", height: 100, marginBottom: 8 }}
        required
      />
      <input
        type="file"
        onChange={(e) => setImage(e.target.files[0])}
        accept="image/*"
        required
      />
      <br />
      <button type="submit" style={{ marginTop: 12 }} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
      {error && (
        <div
          style={{
            marginTop: 12,
            color: "red",
          }}
        >
          {error}
        </div>
      )}
    </form>
  );
};

export default UploadBox;
