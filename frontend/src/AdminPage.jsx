import { useEffect, useState } from "react";
import "./App.css";

function AdminPage() {
  const [tickets, setTickets] = useState([]);

  const fetchTickets = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/tickets"
      );

      if (!response.ok) {
        throw new Error("Failed to fetch tickets");
      }

      const data = await response.json();
      setTickets(data);

    } catch (err) {
      console.log("Ticket fetch error:", err);
    }
  };

  useEffect(() => {
    fetchTickets();
  }, []);

  const getPriorityClass = (priority) => {
    return priority?.toLowerCase() || "";
  };

  const getSentimentClass = (sentiment) => {
    return sentiment?.toLowerCase() || "";
  };

  return (
    <div className="app">
      <header className="header">
        <div className="brand">
          <div className="logo">S</div>
          <div>
            <h1>SmartSupport AI</h1>
            <p>Admin Dashboard</p>
          </div>
        </div>
        <div className="status">
          <span className="status-dot"></span>
          Admin Panel
        </div>
      </header>

      <main className="dashboard">
        <section className="welcome">
          <div>
            <h2>Admin Ticket Queue</h2>
            <p>
              Manage and monitor all customer support tickets.
            </p>
          </div>
        </section>

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
                  <tr key={ticket.id}>
                    <td>#{ticket.id}</td>
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
                      <span className="status-badge">
                        {ticket.status}
                      </span>
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
      </main>

      <footer>
        <p>
          SmartSupport AI • Admin Portal
        </p>
      </footer>

    </div>
  );
}

export default AdminPage;