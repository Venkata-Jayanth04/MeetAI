import { useState } from "react";
import { FaUpload, FaFileAudio } from "react-icons/fa";
import API from "../api";

function UploadSection({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select an audio file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const response = await API.post("/upload", formData);
      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card upload-card">
      <h2>
        <FaUpload /> Upload Meeting Audio
      </h2>

      <div className="upload-controls">
        <label className="file-upload">
          <FaFileAudio />
          <span>
            {file ? file.name : "Select Meeting Audio"}
          </span>

          <input
            type="file"
            accept=".wav,.mp3,.m4a"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </label>

        <button
          className="upload-btn"
          onClick={uploadFile}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Upload Meeting"}
        </button>
      </div>

      {file && (
        <div className="selected-file">
          Selected File: <strong>{file.name}</strong>
        </div>
      )}
    </div>
  );
}

export default UploadSection;