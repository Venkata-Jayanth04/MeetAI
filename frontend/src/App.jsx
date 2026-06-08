import { useState } from "react";
import UploadSection from "./components/UploadSection";
import ResultsSection from "./components/ResultsSection";
import ChatSection from "./components/ChatSection";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={darkMode ? "app dark" : "app"}>
      <div className="header">
        <div>
          <h1>MeetAI</h1>
          <p>
            Transform meetings into insights,
            summaries, action items, and answers.
          </p>
        </div>

        <button
          className="theme-btn"
          onClick={() => setDarkMode(!darkMode)}
        >
          {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
        </button>
      </div>

      <UploadSection setResult={setResult} />

      {result && (
        <>
          <ResultsSection result={result} />
          <ChatSection />
        </>
      )}
    </div>
  );
}

export default App;