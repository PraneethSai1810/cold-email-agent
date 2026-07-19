function EmailOutput({ subject, email, setEmail, sources }) {
  const copyEmail = async () => {
    const fullText = subject ? `Subject: ${subject}\n\n${email}` : email;
    await navigator.clipboard.writeText(fullText);
    alert("Email copied!");
  };

  return (
    <div className="output">
      <h2>Generated Email</h2>

      {subject && (
        <div className="subject-line">
          <strong>Subject:</strong> {subject}
        </div>
      )}

      <textarea
        rows="12"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <button onClick={copyEmail}>
        Copy to Clipboard
      </button>

      {sources && sources.length > 0 && (
        <div className="sources">
          <h3>Sources used</h3>
          <ul>
            {sources.map((s, i) => (
              <li key={i}>
                <a href={s.url} target="_blank" rel="noopener noreferrer">
                  {s.title}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default EmailOutput;