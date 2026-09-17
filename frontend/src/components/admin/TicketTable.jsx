function TicketTable({
  tickets,
  getPriorityClass,
  getSentimentClass,
  updateStatus,
  onTicketClick
}) {
  return (
    <section className="admin-tickets">

      <div className="admin-header">
        <div>
          <h2>All Tickets</h2>

          <p>
            Customer support requests
          </p>
        </div>

        <span className="ticket-count">
          {tickets.length} Tickets
        </span>
      </div>

      <div className="table-container">

        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Customer</th>
              <th>Ticket</th>
              <th>Category</th>
              <th>Priority</th>
              <th>Sentiment</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {tickets.map((ticket) => (
              <tr
                key={ticket.id}
                onClick={() => onTicketClick(ticket)}
                style={{ cursor: "pointer" }}
              >

                <td>
                  #{ticket.id}
                </td>

                <td>
                  <strong>
                    {ticket.customer_name}
                  </strong>
                </td>

                <td className="ticket-text">
                  {ticket.ticket}
                </td>

                <td>
                  {ticket.category}
                </td>

                <td>
                  <span
                    className={`badge ${getPriorityClass(
                      ticket.priority
                    )}`}
                  >
                    {ticket.priority}
                  </span>
                </td>

                <td>
                  <span
                    className={`badge ${getSentimentClass(
                      ticket.sentiment
                    )}`}
                  >
                    {ticket.sentiment}
                  </span>
                </td>

                <td>
                  <select
                    value={ticket.status}
                    onChange={(e) =>
                      updateStatus(
                        ticket.id,
                        e.target.value
                      )
                    }
                  >
                    <option value="Open">
                      Open
                    </option>

                    <option value="In Progress">
                      In Progress
                    </option>

                    <option value="Resolved">
                      Resolved
                    </option>

                    <option value="Escalated">
                      Escalated
                    </option>
                  </select>
                </td>

              </tr>
            ))}
          </tbody>
        </table>

        {tickets.length === 0 && (
          <div className="empty-tickets">
            No tickets available.
          </div>
        )}

      </div>
    </section>
  );
}

export default TicketTable;