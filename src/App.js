import React, { useState } from "react";
import UploadBox from "./components/UploadBox";
import ResultCards from "./components/ResultCards";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h1>Multimodal Analyzer</h1>
      <UploadBox setResults={setResults} />
      {results && <ResultCards results={results} />}
    </div>
  );
}

export default App;
