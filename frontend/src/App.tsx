import "./App.css";

function App() {
  return (
    <main className="app">
      <section className="hero">
        <p className="eyebrow">Enterprise AI Governance Gateway</p>
        <h1>GuardRail AI Dashboard</h1>
        <p className="subtitle">
          Analyze prompts before model invocation, detect sensitive data,
          apply governance policies, and view risk decisions.
        </p>
      </section>

      <section className="dashboard-grid">
        <div className="card">
          <h2>Prompt Analyzer</h2>

          <label htmlFor="userId">User ID</label>
          <input id="userId" type="text" placeholder="user_101" />

          <label htmlFor="department">Department</label>
          <input id="department" type="text" placeholder="Finance" />

          <label htmlFor="prompt">Prompt</label>
          <textarea
            id="prompt"
            rows={7}
            placeholder="Paste a prompt to analyze..."
          />

          <button type="button">Analyze Prompt</button>
        </div>

        <div className="card">
          <h2>Analysis Result</h2>
          <div className="placeholder">
            Submit a prompt to view risk score, action, detections, redacted
            prompt, and cost details.
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;