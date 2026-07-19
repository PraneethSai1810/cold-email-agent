import { useState } from "react";
import API from "../api";

function Form({ onGenerate }) {
  const [resume, setResume] = useState("");
  const [company, setCompany] = useState("");
  const [role, setRole] = useState("");
  const [recipientName, setRecipientName] = useState("");
  const [extracting, setExtracting] = useState(false);

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setExtracting(true);
      const res = await API.post("/extract-resume", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResume(res.data.resume_text);
    } catch (err) {
      alert(
        err.response?.data?.detail ||
        "Couldn't extract text from file. Try pasting manually."
      );
    } finally {
      setExtracting(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    onGenerate({
      resume,
      company,
      role,
      recipient_name: recipientName,
    });
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <div className="file-upload">
        <label htmlFor="resume-file">Upload Resume (PDF or DOCX)</label>
        <input
          type="file"
          id="resume-file"
          accept=".pdf,.docx"
          onChange={handleFileChange}
        />
        {extracting && <p>Extracting text...</p>}
      </div>

      <textarea
        placeholder="Paste your resume, or upload a file above..."
        rows="10"
        value={resume}
        onChange={(e) => setResume(e.target.value)}
        required
      />

      <input
        type="text"
        placeholder="Target Company"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
        required
      />

      <input
        type="text"
        placeholder="Target Role (Optional)"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <input
        type="text"
        placeholder="Recipient Name (Optional)"
        value={recipientName}
        onChange={(e) => setRecipientName(e.target.value)}
      />

      <button type="submit">
        Generate Email
      </button>
    </form>
  );
}

export default Form;