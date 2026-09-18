import "./CategoryStats.css";

function CategoryStats({
  totalTickets,
  openTickets,
  inProgressTickets,
  resolvedTickets,
  escalatedTickets,
  averageResolution
}) {
  return (
    <section className="category-kpi-grid">
      <div className="category-kpi-card">
        <span>Total Tickets</span>
        <strong>{totalTickets}</strong>
        <small>Tickets in this category</small>
      </div>

      <div className="category-kpi-card">
        <span>Open</span>
        <strong>{openTickets}</strong>
        <small>Currently open</small>
      </div>

      <div className="category-kpi-card">
        <span>In Progress</span>
        <strong>{inProgressTickets}</strong>
        <small>Being handled</small>
      </div>

      <div className="category-kpi-card">
        <span>Resolved</span>
        <strong>{resolvedTickets}</strong>
        <small>Successfully resolved</small>
      </div>

      <div className="category-kpi-card">
        <span>Escalated</span>
        <strong>{escalatedTickets}</strong>
        <small>Requires attention</small>
      </div>


      <div className="category-kpi-card">
        <span>Avg. Resolution</span>
        <strong>{averageResolution}h</strong>
        <small>Estimated handling time</small>
      </div>
    </section>
  );
}

export default CategoryStats;

