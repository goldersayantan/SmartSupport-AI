import "./TicketAnalysis.css";

function TicketAnalysis({ result }) {
  const getPriorityClass = (priority) => {
    return priority?.toLowerCase() || "";
  };

  const getSentimentClass = (sentiment) => {
    return sentiment?.toLowerCase() || "";
  };

  return (
    <section className="ticket-analysis">
      <div className="analysis-header">
        <div>
          <span className="analysis-label">AI RESULT</span>
          <h2>Ticket Analysis</h2>
          <p>Your support request has been analyzed successfully.</p>
        </div>

        <div className="analysis-success">✓ Analysis Complete</div>
      </div>

      <div className="analysis-grid">
        <div className="analysis-card">
          <div className="analysis-card-icon category">◎</div>

          <div>
            <span>Category</span>
            <strong>{result.category}</strong>
            <small>Detected issue type</small>
          </div>
        </div>

        <div className="analysis-card">
          <div className="analysis-card-icon priority">!</div>
          <div>
            <span>Priority</span>
            <strong
              className={`analysis-badge ${getPriorityClass(
                result.priority
              )}`}
            >
              {result.priority}
            </strong>
            <small>Recommended urgency</small>
          </div>
        </div>

        <div className="analysis-card">
          <div className="analysis-card-icon sentiment">♡</div>
          <div>
            <span>Sentiment</span>
            <strong
              className={`analysis-badge ${getSentimentClass(
                result.sentiment
              )}`}
            >
              {result.sentiment}
            </strong>
            <small>Customer emotional tone</small>
          </div>
        </div>

        <div className="analysis-card">
          <div className="analysis-card-icon time">◷</div>
          <div>
            <span>Estimated Resolution</span>
            <strong>{result.resolution_time_hours} hours</strong>
            <small>Estimated handling time</small>
          </div>
        </div>
      </div>

      <div className="submitted-ticket">
        <span>Submitted Ticket</span>
        <p>"{result.ticket}"</p>
      </div>
    </section>
  );
}

export default TicketAnalysis;
