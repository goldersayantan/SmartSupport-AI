import "./FilteredTickets.css";

function FilteredTickets({
  tickets,
  selectedCategory,
  selectedFilter,
  setSelectedFilter,
  onTicketClick
}) {
  if (!selectedFilter || !selectedCategory) {
    return null;
  }

  const categoryTickets = tickets.filter(
    (ticket) => ticket.category === selectedCategory
  );

  const filteredTickets = categoryTickets.filter(
    (ticket) =>
      ticket.sentiment === selectedFilter ||
      ticket.priority === selectedFilter
  );

  return (
    <div className="filtered-tickets">

      <div className="filtered-header">
        <div>
          <h3>{selectedFilter} Tickets</h3>

          <p>
            {filteredTickets.length} ticket(s) found
          </p>
        </div>

        <button
          className="clear-filter"
          onClick={() => setSelectedFilter(null)}
        >
          Clear Filter
        </button>
      </div>

      <div className="filtered-ticket-list">

        {filteredTickets.map((ticket) => (
          <div
            className="filtered-ticket"
            key={ticket.id}
            onClick={() => onTicketClick(ticket)}
            style={{ cursor: "pointer" }}
          >

            <div className="filtered-ticket-top">
              <strong>
                #{ticket.id} — {ticket.customer_name}
              </strong>

              <span className="ticket-status">
                {ticket.status}
              </span>
            </div>

            <p className="filtered-ticket-text">
              {ticket.ticket}
            </p>

            <div className="filtered-ticket-meta">
              <span>{ticket.category}</span>

              <span>{ticket.priority}</span>

              <span>{ticket.sentiment}</span>

              <span>
                {ticket.resolution_time_hours}h estimated
              </span>
            </div>

          </div>
        ))}

        {filteredTickets.length === 0 && (
          <div className="empty-tickets">
            No tickets found for this filter.
          </div>
        )}

      </div>

    </div>
  );
}

export default FilteredTickets;