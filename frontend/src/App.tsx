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

type GatewayResult = {
  action?: string;
  risk_score?: number;
  risk_level?: string;
  redacted_prompt?: string;
  detections?: Detections;
  risk_reasons?: string[];
  selected_model?: string;
  model_called?: boolean;
  ai_response?: string;
  response?: string;
  message?: string;
  estimated_tokens?: number;
  estimated_cost?: number;
  blocked_cost_savings?: number;
};

type DepartmentSummaryRow = {
  department: string;
  total_requests?: number;
  request_count?: number;
  blocked_count?: number;
  critical_count?: number;
  top_risk_reasons?: string[] | Record<string, number>;
};

type RecentAuditLog = {
  id?: number;
  user_id?: string;
  department?: string;
  action?: string;
  risk_score?: number;
  risk_level?: string;
  redacted_prompt?: string;
  estimated_cost?: number;
  blocked_cost_savings?: number;
  created_at?: string;
  timestamp?: string;
};

type AuditSummary = {
  total_logs?: number;
  total_requests?: number;
  blocked_count?: number;
  warning_count?: number;
  warn_count?: number;
  critical_count?: number;
  total_estimated_cost?: number;
  total_blocked_savings?: number;
  recent_logs?: RecentAuditLog[];
  logs?: RecentAuditLog[];
};

function formatCost(value?: number) {
  if (typeof value !== "number") {
    return "N/A";
  }

  return `$${value.toFixed(6)}`;
}

function formatLabel(label: string) {
  const labelMap: Record<string, string> = {
    ssn: "SSN",
    email: "Email",
    phone: "Phone",
    credit_card: "Credit Card",
    password: "Password",
    api_key: "API Key",
    prompt_injection: "Prompt Injection",
  };

  return labelMap[label] || label;
}

function sumLogValues(
  logs: RecentAuditLog[],
  key: "estimated_cost" | "blocked_cost_savings"
) {
  return logs.reduce((total, log) => total + (log[key] ?? 0), 0);
}

function App() {
  const [userId, setUserId] = useState("user_101");
  const [department, setDepartment] = useState("Finance");
  const [prompt, setPrompt] = useState("");

  const [result, setResult] = useState<AnalyzeResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [gatewayPrompt, setGatewayPrompt] = useState("");
  const [gatewayResult, setGatewayResult] = useState<GatewayResult | null>(
    null
  );
  const [isGatewayLoading, setIsGatewayLoading] = useState(false);
  const [gatewayError, setGatewayError] = useState("");

  const [departmentSummary, setDepartmentSummary] = useState<
    DepartmentSummaryRow[]
  >([]);
  const [isDepartmentLoading, setIsDepartmentLoading] = useState(false);
  const [departmentError, setDepartmentError] = useState("");

  const [auditSummary, setAuditSummary] = useState<AuditSummary | null>(null);
  const [isAuditLoading, setIsAuditLoading] = useState(false);
  const [auditError, setAuditError] = useState("");

  const auditLogs = auditSummary?.recent_logs || auditSummary?.logs || [];

  const calculatedEstimatedCost =
    auditSummary?.total_estimated_cost ??
    sumLogValues(auditLogs, "estimated_cost");

  const calculatedBlockedSavings =
    auditSummary?.total_blocked_savings ??
    sumLogValues(auditLogs, "blocked_cost_savings");

  async function handleAnalyze() {
    if (!prompt.trim()) {
      setErrorMessage("Please enter a prompt before analyzing.");
      return;
    }

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

  async function handleGateway() {
    if (!gatewayPrompt.trim()) {
      setGatewayError("Please enter a gateway prompt before running the gateway.");
      return;
    }

    setIsGatewayLoading(true);
    setGatewayError("");
    setGatewayResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/gateway", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": "guardrail-local-dev-key",
        },
        body: JSON.stringify({
          prompt: gatewayPrompt,
          user_id: userId,
          department: department,
        }),
      });

      if (!response.ok) {
        throw new Error("Gateway request failed");
      }

      const data: GatewayResult = await response.json();
      setGatewayResult(data);
    } catch (error) {
      setGatewayError(
        "Could not connect to the gateway endpoint. Make sure FastAPI is running on port 8000."
      );
    } finally {
      setIsGatewayLoading(false);
    }
  }

  async function handleLoadDepartmentSummary() {
    setIsDepartmentLoading(true);
    setDepartmentError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/department-summary", {
        method: "GET",
        headers: {
          "x-api-key": "guardrail-local-dev-key",
        },
      });

      if (!response.ok) {
        throw new Error("Department summary request failed");
      }

      const data = await response.json();

      const rows = Array.isArray(data)
        ? data
        : data.departments || data.department_summary || [];

      setDepartmentSummary(rows);
    } catch (error) {
      setDepartmentError(
        "Could not load department summary. Make sure FastAPI is running on port 8000."
      );
    } finally {
      setIsDepartmentLoading(false);
    }
  }

  async function handleLoadAuditSummary() {
    setIsAuditLoading(true);
    setAuditError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/audit-summary", {
        method: "GET",
        headers: {
          "x-api-key": "guardrail-local-dev-key",
        },
      });

      if (!response.ok) {
        throw new Error("Audit summary request failed");
      }

      const data: AuditSummary = await response.json();
      setAuditSummary(data);
    } catch (error) {
      setAuditError(
        "Could not load audit summary. Make sure FastAPI is running on port 8000."
      );
    } finally {
      setIsAuditLoading(false);
    }
  }

  return (
    <main className="app">
      <section className="hero">
        <p className="eyebrow">Enterprise AI Governance Gateway</p>
        <h1>GuardRail AI Dashboard</h1>
        <p className="subtitle">
          Analyze prompts before model invocation, detect sensitive data, apply
          governance policies, and view risk decisions.
        </p>
      </section>

      <section className="top-metrics">
        <div className="metric-card">
          <span>Total Logs</span>
          <strong>
            {auditSummary?.total_logs ?? auditSummary?.total_requests ?? 0}
          </strong>
        </div>

        <div className="metric-card">
          <span>Blocked</span>
          <strong>{auditSummary?.blocked_count ?? 0}</strong>
        </div>

        <div className="metric-card">
          <span>Warnings</span>
          <strong>
            {auditSummary?.warning_count ?? auditSummary?.warn_count ?? 0}
          </strong>
        </div>

        <div className="metric-card">
          <span>Critical</span>
          <strong>{auditSummary?.critical_count ?? 0}</strong>
        </div>

        <div className="metric-card">
          <span>Estimated Cost</span>
          <strong>{formatCost(calculatedEstimatedCost)}</strong>
        </div>

        <div className="metric-card">
          <span>Blocked Savings</span>
          <strong>{formatCost(calculatedBlockedSavings)}</strong>
        </div>
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
                  {formatCost(result.estimated_cost)}
                </p>
                <p>
                  <strong>Blocked Savings:</strong>{" "}
                  {formatCost(result.blocked_cost_savings)}
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
                    {formatLabel(key)}: {String(value)}
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

      <section className="wide-card">
        <div className="card">
          <h2>Gateway Demo</h2>
          <p className="section-note">
            This simulates the real AI gateway flow. Safe prompts can reach the
            model. Risky prompts are blocked before model invocation.
          </p>

          <label htmlFor="gatewayPrompt">Gateway Prompt</label>
          <textarea
            id="gatewayPrompt"
            rows={6}
            value={gatewayPrompt}
            onChange={(event) => setGatewayPrompt(event.target.value)}
            placeholder="Ask a safe question or paste a risky prompt..."
          />

          <button
            type="button"
            onClick={handleGateway}
            disabled={isGatewayLoading}
          >
            {isGatewayLoading ? "Running Gateway..." : "Run Gateway"}
          </button>

          {gatewayError && <div className="error-box">{gatewayError}</div>}

          {gatewayResult && (
            <div className="gateway-result">
              <h3>Gateway Result</h3>

              {gatewayResult.action && (
                <div
                  className={`action-pill ${gatewayResult.action.toLowerCase()}`}
                >
                  {gatewayResult.action}
                </div>
              )}

              <div className="result-grid">
                <p>
                  <strong>Model Called:</strong>{" "}
                  {String(gatewayResult.model_called ?? "N/A")}
                </p>
                <p>
                  <strong>Selected Model:</strong>{" "}
                  {gatewayResult.selected_model || "N/A"}
                </p>
                <p>
                  <strong>Risk Score:</strong>{" "}
                  {gatewayResult.risk_score ?? "N/A"}
                </p>
                <p>
                  <strong>Risk Level:</strong>{" "}
                  {gatewayResult.risk_level || "N/A"}
                </p>
                <p>
                  <strong>Estimated Cost:</strong>{" "}
                  {formatCost(gatewayResult.estimated_cost)}
                </p>
                <p>
                  <strong>Blocked Savings:</strong>{" "}
                  {formatCost(gatewayResult.blocked_cost_savings)}
                </p>
              </div>

              <h3>Redacted Prompt</h3>
              <p className="submitted-prompt">
                {gatewayResult.redacted_prompt || "N/A"}
              </p>

              <h3>AI / Gateway Response</h3>
              <p className="submitted-prompt">
                {gatewayResult.ai_response ||
                  gatewayResult.response ||
                  gatewayResult.message ||
                  "No response returned."}
              </p>

              <h3>Risk Reasons</h3>
              {gatewayResult.risk_reasons &&
              gatewayResult.risk_reasons.length > 0 ? (
                <ul>
                  {gatewayResult.risk_reasons.map((reason) => (
                    <li key={reason}>{reason}</li>
                  ))}
                </ul>
              ) : (
                <p>No risk reasons returned.</p>
              )}
            </div>
          )}
        </div>
      </section>

      <section className="wide-card">
        <div className="card">
          <h2>Department Summary</h2>
          <p className="section-note">
            View department-level AI governance metrics such as total requests,
            blocked prompts, critical risks, and top risk reasons.
          </p>

          <button
            type="button"
            onClick={handleLoadDepartmentSummary}
            disabled={isDepartmentLoading}
          >
            {isDepartmentLoading
              ? "Loading Summary..."
              : "Load Department Summary"}
          </button>

          {departmentError && (
            <div className="error-box">{departmentError}</div>
          )}

          {departmentSummary.length > 0 ? (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Department</th>
                    <th>Total Requests</th>
                    <th>Blocked</th>
                    <th>Critical</th>
                    <th>Top Risk Reasons</th>
                  </tr>
                </thead>
                <tbody>
                  {departmentSummary.map((row) => (
                    <tr key={row.department}>
                      <td>{row.department}</td>
                      <td>{row.total_requests ?? row.request_count ?? 0}</td>
                      <td>{row.blocked_count ?? 0}</td>
                      <td>{row.critical_count ?? 0}</td>
                      <td>
                        {Array.isArray(row.top_risk_reasons)
                          ? row.top_risk_reasons.join(", ")
                          : row.top_risk_reasons
                          ? Object.entries(row.top_risk_reasons)
                              .map(([reason, count]) => `${reason}: ${count}`)
                              .join(", ")
                          : "N/A"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            !departmentError && (
              <div className="placeholder summary-placeholder">
                Load department summary to view enterprise AI governance
                metrics.
              </div>
            )
          )}
        </div>
      </section>

      <section className="wide-card">
        <div className="card">
          <h2>Audit Summary</h2>
          <p className="section-note">
            Review audit-level governance metrics, recent prompt decisions, cost
            tracking, and blocked cost savings.
          </p>

          <button
            type="button"
            onClick={handleLoadAuditSummary}
            disabled={isAuditLoading}
          >
            {isAuditLoading
              ? "Loading Audit Summary..."
              : "Load Audit Summary"}
          </button>

          {auditError && <div className="error-box">{auditError}</div>}

          {auditSummary ? (
            <div className="audit-section">
              <div className="metric-grid">
                <div className="metric-card">
                  <span>Total Logs</span>
                  <strong>
                    {auditSummary.total_logs ?? auditSummary.total_requests ?? 0}
                  </strong>
                </div>

                <div className="metric-card">
                  <span>Blocked</span>
                  <strong>{auditSummary.blocked_count ?? 0}</strong>
                </div>

                <div className="metric-card">
                  <span>Warnings</span>
                  <strong>
                    {auditSummary.warning_count ?? auditSummary.warn_count ?? 0}
                  </strong>
                </div>

                <div className="metric-card">
                  <span>Critical</span>
                  <strong>{auditSummary.critical_count ?? 0}</strong>
                </div>

                <div className="metric-card">
                  <span>Total Estimated Cost</span>
                  <strong>{formatCost(calculatedEstimatedCost)}</strong>
                </div>

                <div className="metric-card">
                  <span>Total Blocked Savings</span>
                  <strong>{formatCost(calculatedBlockedSavings)}</strong>
                </div>
              </div>

              <h3>Recent Audit Logs</h3>

              {auditLogs.length > 0 ? (
                <div className="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>User</th>
                        <th>Department</th>
                        <th>Action</th>
                        <th>Risk</th>
                        <th>Cost</th>
                        <th>Blocked Savings</th>
                        <th>Redacted Prompt</th>
                      </tr>
                    </thead>
                    <tbody>
                      {auditLogs.map((log, index) => (
                        <tr key={log.id ?? index}>
                          <td>{log.user_id || "N/A"}</td>
                          <td>{log.department || "N/A"}</td>
                          <td>{log.action || "N/A"}</td>
                          <td>
                            {log.risk_score ?? "N/A"}{" "}
                            {log.risk_level ? `(${log.risk_level})` : ""}
                          </td>
                          <td>{formatCost(log.estimated_cost)}</td>
                          <td>{formatCost(log.blocked_cost_savings)}</td>
                          <td>{log.redacted_prompt || "N/A"}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              ) : (
                <div className="placeholder summary-placeholder">
                  No recent audit logs returned.
                </div>
              )}
            </div>
          ) : (
            !auditError && (
              <div className="placeholder summary-placeholder">
                Load audit summary to view traceability and governance metrics.
              </div>
            )
          )}
        </div>
      </section>
    </main>
  );
}

export default App;