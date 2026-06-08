import {
  FaFileAlt,
  FaSmile,
  FaTasks,
  FaUsers
} from "react-icons/fa";

function ResultsSection({ result }) {
  if (!result) return null;

  const sentiment = result.sentiment?.[0];

  return (
    <>
      <div className="card">
        <h2>
          <FaFileAlt /> Transcript
        </h2>
        <p>{result.transcript}</p>
      </div>

      <div className="card">
        <h2>
          <FaFileAlt /> Summary
        </h2>
        <p>{result.summary}</p>
      </div>

      <div className="grid">
        <div className="card">
          <h2>
            <FaSmile /> Sentiment
          </h2>

          <span
            className={`badge ${
              sentiment?.label === "POSITIVE"
                ? "positive"
                : sentiment?.label === "NEGATIVE"
                ? "negative"
                : "neutral"
              }`}
          >
            {sentiment?.label}
          </span>

          <p>
            Confidence:{" "}
            {sentiment?.score?.toFixed(3)}
          </p>
        </div>

        <div className="card">
          <h2>
            <FaUsers /> Entities
          </h2>

          <div className="entity-section">
            <h4>People</h4>
            {result.entities?.people?.map(
              (item, index) => (
                <span
                  key={index}
                  className="chip"
                >
                  {item}
                </span>
              )
            )}
          </div>

          <div className="entity-section">
            <h4>Organizations</h4>
            {result.entities?.organizations?.map(
              (item, index) => (
                <span
                  key={index}
                  className="chip"
                >
                  {item}
                </span>
              )
            )}
          </div>

          <div className="entity-section">
            <h4>Locations</h4>
            {result.entities?.locations?.map(
              (item, index) => (
                <span
                  key={index}
                  className="chip"
                >
                  {item}
                </span>
              )
            )}
          </div>
        </div>
      </div>

      <div className="card">
        <h2>
          <FaTasks /> Action Items
        </h2>

        <pre>{result.action_items}</pre>
      </div>
    </>
  );
}

export default ResultsSection;