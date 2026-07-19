import { useState } from "react";
import API from "./api";
import Form from "./components/Form";
import EmailOutput from "./components/EmailOutput";
import Spinner from "./components/Spinner";

function App() {
  const [loading, setLoading] = useState(false);
  const [subject, setSubject] = useState("");
  const [email, setEmail] = useState("");
  const [sources, setSources] = useState([]);

  const generateEmail = async (formData) => {
    try {
      setLoading(true);
      const res = await API.post("/generate-email", formData);
      setSubject(res.data.subject);
      setEmail(res.data.email);
      setSources(res.data.sources || []);
    } catch (err) {
      alert(err.response?.data?.detail || "Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page fade-in">
      <div className="hero">
        <svg className="mailbox-icon" viewBox="0 0 48 48" fill="none">
  <rect x="6" y="10" width="36" height="28" rx="3" stroke="#EDEBE6" strokeWidth="1.8"/>
  <path d="M6 12 L24 26 L42 12" stroke="#C9A860" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
</svg>
        <h1>Cold Email Agent</h1>
        <p>Cold outreach, backed by real research.</p>
      </div>

      <div className="layout">
        <div className="left-col">
          <Form onGenerate={generateEmail} />
        </div>

        <div className="right-col">
          {loading && <Spinner />}
          {!loading && email && (
            <EmailOutput subject={subject} email={email} setEmail={setEmail} sources={sources} />
          )}
          {!loading && !email && (
            <div className="placeholder">Your generated email will appear here.</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;