import { useState } from "react";
import "./App.css";

type Detections = {
  ssn?: boolean;
  email?: boolean;
  phone?: boolean;
  credit_card?: boolean;
  password?: boolean;
  api_key?: boolean;
  prompt_injection?: boolean;
};

type AnalyzeResult = {
  action: string;
  risk_score: number;
  risk_level?: string;
  redacted_prompt: string;
  detections: Detections;
  risk_reasons?: string[];
  estimated_tokens?: number;
  estimated_cost?: number;
  blocked_cost_savings?: number;
};

function App() {
  const [userId, setUserId] = useState("user_101");
  const [department, setDepartment] = useState("Finance");
  const [prompt, setPrompt] = useState("");

  const [result, setResult] = useState<AnalyzeResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  async function handleAnalyze() {
    setIsLoading(true);
    setErrorMessage("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": "guardrail-local-dev-key",
        },
        body: JSON.stringify({
          prompt: prompt,
          user_id: userId,
          department: department,
        }),
      });

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data: AnalyzeResult = await response.json();
      setResult(data);
    } catch (error) {
      setErrorMessage(
        "Could not connect to the backend. Make sure FastAPI is running on port 8000."
      );
    } finally {
      setIsLoading(false);
    }
  }

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
          <input
            id="userId"
            type="text"
            value={userId}
            onChange={(event) => setUserId(event.target.value)}
            placeholder="user_101"
          />

          <label htmlFor="department">Department</label>
          <input
            id="department"
            type="text"
            value={department}
            onChange={(event) => setDepartment(event.target.value)}
            placeholder="Finance"
          />

          <label htmlFor="prompt">Prompt</label>
          <textarea
            id="prompt"
            rows={7}
            value={prompt}
            onChange={(event) => setPrompt(event.target.value)}
            placeholder="Paste a prompt to analyze..."
          />

          <button type="button" onClick={handleAnalyze} disabled={isLoading}>
            {isLoading ? "Analyzing..." : "Analyze Prompt"}
          </button>
        </div>

        <div className="card">
          <h2>Analysis Result</h2>

          {errorMessage && <div className="error-box">{errorMessage}</div>}

          {result ? (
            <div className="result-box">
              <div className={`action-pill ${result.action.toLowerCase()}`}>
                {result.action}
              </div>

              <div className="result-grid">
                <p>
                  <strong>Risk Score:</strong> {result.risk_score}
                </p>
                <p>
                  <strong>Risk Level:</strong> {result.risk_level || "N/A"}
                </p>
                <p>
                  <strong>Estimated Tokens:</strong>{" "}
                  {result.estimated_tokens ?? "N/A"}
                </p>
                <p>
                  <strong>Estimated Cost:</strong>{" "}
                  {result.estimated_cost ?? "N/A"}
                </p>
                <p>
                  <strong>Blocked Savings:</strong>{" "}
                  {result.blocked_cost_savings ?? "N/A"}
                </p>
              </div>

              <h3>Redacted Prompt</h3>
              <p className="submitted-prompt">{result.redacted_prompt}</p>

              <h3>Detections</h3>
              <div className="detection-list">
                {Object.entries(result.detections).map(([key, value]) => (
                  <span
                    key={key}
                    className={value ? "detection active" : "detection"}
                  >
                    {key}: {String(value)}
                  </span>
                ))}
              </div>

              <h3>Risk Reasons</h3>
              {result.risk_reasons && result.risk_reasons.length > 0 ? (
                <ul>
                  {result.risk_reasons.map((reason) => (
                    <li key={reason}>{reason}</li>
                  ))}
                </ul>
              ) : (
                <p>No risk reasons returned.</p>
              )}
            </div>
          ) : (
            !errorMessage && (
              <div className="placeholder">
                Submit a prompt to view risk score, action, detections,
                redacted prompt, and cost details.
              </div>
            )
          )}
        </div>
      </section>
    </main>
  );
}

export default App;