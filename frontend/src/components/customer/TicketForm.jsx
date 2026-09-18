import "./TicketForm.css";

function TicketForm({
  ticket,
  setTicket,
  customerName,
  setCustomerName,
  loading,
  error,
  onAnalyze,
}) {
  return (
    <section className="ticket-form-card">

      <div className="ticket-form-heading">

        <div className="ticket-form-icon">
          ✦
        </div>

        <div>
          <h3>Submit a Support Ticket</h3>

          <p>
            Describe your issue and our AI will analyze it
            automatically.
          </p>
        </div>

      </div>

      <div className="ticket-form-body">

        <label>
          Your Name
        </label>

        <input
          type="text"
          value={customerName}
          onChange={(event) =>
            setCustomerName(event.target.value)
          }
          placeholder="Enter your name..."
        />

        <label>
          Support Request
        </label>

        <textarea
          value={ticket}
          onChange={(event) =>
            setTicket(event.target.value)
          }
          placeholder="Example: My package has been delayed for three days..."
          rows="7"
        />

        <div className="ticket-form-footer">

          <span className="ticket-character-count">
            {ticket.length} characters
          </span>

          <button
            type="button"
            className="analyze-ticket-button"
            onClick={onAnalyze}
            disabled={loading}
          >
            {loading ? (
              <>
                <span className="ticket-spinner"></span>
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

        {error && (
          <div className="ticket-form-error">
            {error}
          </div>
        )}

      </div>

    </section>
  );
}

export default TicketForm;
