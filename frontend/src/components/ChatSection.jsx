import { useState } from "react";
import { FaRobot, FaPaperPlane } from "react-icons/fa";
import API from "../api";

function ChatSection() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);

    try {
      const response = await API.post("/chat", {
        question,
      });

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      alert("Failed to get answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>
        <FaRobot /> Chat With Meeting
      </h2>

      <div className="chat-input-container">
        <input
          type="text"
          placeholder="Ask anything about the meeting..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          className="ask-btn"
          onClick={askQuestion}
          disabled={loading}
        >
          <FaPaperPlane />

          {loading ? " Thinking..." : " Ask"}
        </button>
      </div>

      {answer && (
        <div className="answer-box">
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default ChatSection;