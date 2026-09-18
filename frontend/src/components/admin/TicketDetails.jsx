import "./TicketDetails.css";

function TicketDetails({
  ticket,
  onBack,
  updateStatus
}) {
  if (!ticket) {
    return null;
  }

  return (
    <section className="ticket-details">

      <div className="ticket-details-header">
        <div>
          <h2>Ticket #{ticket.id}</h2>
          <p>Customer support ticket details</p>
        </div>

        <button
          className="back-button"
          onClick={onBack}
        >
          ← Back to Tickets
        </button>
      </div>

      <div className="ticket-details-card">

        <div className="ticket-details-top">
          <div>
            <span className="detail-label">Customer</span>
            <h3>{ticket.customer_name}</h3>
          </div>

          <span className="ticket-status">{ticket.status}</span>
        </div>

        <div className="ticket-details-message">
          <span className="detail-label">Ticket</span>
          <p>{ticket.ticket}</p>
        </div>

        <div className="ticket-details-grid">
          <div className="detail-item">
            <span className="detail-label">Category</span>
            <strong>{ticket.category}</strong>
          </div>

          <div className="detail-item">
            <span className="detail-label">Priority</span>
            <strong>{ticket.priority}</strong>
          </div>

          <div className="detail-item">
            <span className="detail-label">Sentiment</span>
            <strong>{ticket.sentiment}</strong>
          </div>

          <div className="detail-item">
            <span className="detail-label">Estimated Resolution</span>
            <strong>{ticket.resolution_time_hours} hours</strong>
          </div>

          <div className="detail-item">
            <span className="detail-label">Status</span>
            <select
                value={ticket.status}
                onChange={(e) =>
                updateStatus(
                    ticket.id,
                    e.target.value
                )
                }
            >
                <option value="Open">Open</option>
                <option value="In Progress">In Progress</option>
                <option value="Resolved">Resolved</option>
                <option value="Escalated">Escalated</option>
            </select>
            </div>

          <div className="detail-item">
            <span className="detail-label">Created</span>
            <strong>
              {ticket.created_at
                ? new Date(ticket.created_at).toLocaleString()
                : "Not available"}
            </strong>
          </div>
        </div>
      </div>
    </section>
  );
}

export default TicketDetails;