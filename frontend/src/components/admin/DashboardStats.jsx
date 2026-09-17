import "./DashboardStats.css";

function DashboardStats({
  totalTickets,
  openTickets,
  inProgressTickets,
  resolvedTickets,
  escalatedTickets
}) {
  return (
    <section className="stats-grid">

      <div className="stat-card">
        <span className="stat-label">Total Tickets</span>
        <strong>{totalTickets}</strong>
      </div>

      <div className="stat-card">
        <span className="stat-label">Open</span>
        <strong>{openTickets}</strong>
      </div>

      <div className="stat-card">
        <span className="stat-label">In Progress</span>
        <strong>{inProgressTickets}</strong>
      </div>

      <div className="stat-card">
        <span className="stat-label">Resolved</span>
        <strong>{resolvedTickets}</strong>
      </div>

      <div className="stat-card">
        <span className="stat-label">Escalated</span>
        <strong>{escalatedTickets}</strong>
      </div>

    </section>
  );
}

export default DashboardStats;