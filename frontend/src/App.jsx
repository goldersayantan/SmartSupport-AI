import { useState } from "react";
import "./App.css";

function App() {
  const [ticket, setTicket] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const exampleTickets = [
    "My package has been delayed for three days",
    "Someone used my account and I cannot log in",
    "My payment failed but money was deducted",
    "I want to change my email address",
  ];

  const analyzeTicket = async () => {
    if (!ticket.trim()) {
      setError("Please enter a support ticket.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ticket: ticket,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to analyze ticket.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(
        "Unable to connect to SmartSupport AI. Make sure the FastAPI server is running."
      );
      console.log(err)
    } finally {
      setLoading(false);
    }
  };

  const getPriorityClass = (priority) => {
    return priority?.toLowerCase() || "";
  };

  const getSentimentClass = (sentiment) => {
    return sentiment?.toLowerCase() || "";
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div className="brand">
          <div className="logo">S</div>

          <div>
            <h1>SmartSupport AI</h1>
            <p>AI-powered customer support intelligence</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI System Online
        </div>
      </header>


      {/* Main */}
      <main className="dashboard">

        {/* Welcome */}
        <section className="welcome">
          <div>
            <h2>Analyze a Support Ticket</h2>
            <p>
              Let AI automatically understand, classify and prioritize
              customer support requests.
            </p>
          </div>
        </section>


        {/* Ticket Input */}
        <section className="ticket-card">

          <div className="section-title">
            <div>
              <h3>Customer Ticket</h3>
              <p>Enter the customer's support request below.</p>
            </div>
          </div>

          <textarea
            value={ticket}
            onChange={(e) => setTicket(e.target.value)}
            placeholder="Example: My package has been delayed for three days..."
            rows="7"
          />

          <div className="input-footer">

            <span className="character-count">
              {ticket.length} characters
            </span>

            <button
              className="analyze-button"
              onClick={analyzeTicket}
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="spinner"></span>
                  Analyzing...
                </>
              ) : (
                <>
                  Analyze Ticket
                  <span>→</span>
                </>
              )}
            </button>

          </div>

          {error && <p className="error">{error}</p>}

        </section>


        {/* Examples */}
        <section className="examples">

          <div className="examples-title">
            <span>💡</span>
            Try an example
          </div>

          <div className="example-list">

            {exampleTickets.map((example, index) => (
              <button
                key={index}
                className="example-button"
                onClick={() => setTicket(example)}
              >
                {example}
              </button>
            ))}

          </div>

        </section>


        {/* Results */}
        {result && (
          <section className="results">

            <div className="results-header">
              <div>
                <h2>AI Analysis</h2>
                <p>SmartSupport AI analysis results</p>
              </div>

              <div className="success-badge">
                ✓ Analysis Complete
              </div>
            </div>


            <div className="result-grid">

              {/* Category */}
              <div className="result-card">

                <div className="card-icon category-icon">
                  ◎
                </div>

                <div className="card-content">
                  <span>Category</span>
                  <strong>{result.category}</strong>
                  <small>Detected issue type</small>
                </div>

              </div>


              {/* Priority */}
              <div className="result-card">

                <div className="card-icon priority-icon">
                  !
                </div>

                <div className="card-content">
                  <span>Priority</span>

                  <strong
                    className={`badge ${getPriorityClass(result.priority)}`}
                  >
                    {result.priority}
                  </strong>

                  <small>Recommended urgency</small>
                </div>

              </div>


              {/* Sentiment */}
              <div className="result-card">

                <div className="card-icon sentiment-icon">
                  ♡
                </div>

                <div className="card-content">
                  <span>Sentiment</span>

                  <strong
                    className={`badge ${getSentimentClass(
                      result.sentiment
                    )}`}
                  >
                    {result.sentiment}
                  </strong>

                  <small>Customer emotional tone</small>
                </div>

              </div>


              {/* Resolution */}
              <div className="result-card">

                <div className="card-icon time-icon">
                  ◷
                </div>

                <div className="card-content">
                  <span>Estimated Resolution</span>

                  <strong>
                    {result.resolution_time_hours} hours
                  </strong>

                  <small>Estimated handling time</small>
                </div>

              </div>

            </div>


            {/* Ticket Summary */}
            <div className="ticket-summary">

              <span>Analyzed Ticket</span>

              <p>
                "{result.ticket}"
              </p>

            </div>

          </section>
        )}

      </main>

      {/* Footer */}
      <footer>
        <p>
          SmartSupport AI • Intelligent Customer Support
        </p>
      </footer>

    </div>
  );
}

export default App;