import "./CategoryTicketExplorer.css";

function CategoryTicketExplorer({
  sentimentData,
  priorityData,
  selectedFilter,
  setSelectedFilter,
  filteredTickets,
  onTicketClick
}) {
  return (
    <section className="category-ticket-explorer">

      {/* Header */}

      <div className="ticket-explorer-header">

        <div>

          <span>
            Ticket Explorer
          </span>

          <h3>
            {selectedFilter
              ? `${selectedFilter} Tickets`
              : "Explore Category Tickets"}
          </h3>

          <p>
            Select a sentiment or priority to
            view matching tickets.
          </p>

        </div>


        {selectedFilter && (

          <button
            className="clear-category-filter"
            onClick={() =>
              setSelectedFilter(null)
            }
          >
            Clear Filter
          </button>

        )}

      </div>


      {/* Sentiment */}

      <div className="ticket-filter-group">

        <div className="ticket-filter-heading">

          <h4>
            Sentiment
          </h4>

          <span>
            Customer emotional tone
          </span>

        </div>


        <div className="ticket-filter-grid">

          <div
            className={`ticket-filter-card negative ${
              selectedFilter === "Negative"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("Negative")
            }
          >

            <span>
              Negative
            </span>

            <strong>
              {sentimentData[0].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>


          <div
            className={`ticket-filter-card neutral ${
              selectedFilter === "Neutral"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("Neutral")
            }
          >

            <span>
              Neutral
            </span>

            <strong>
              {sentimentData[1].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>


          <div
            className={`ticket-filter-card positive ${
              selectedFilter === "Positive"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("Positive")
            }
          >

            <span>
              Positive
            </span>

            <strong>
              {sentimentData[2].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>

        </div>

      </div>


      {/* Priority */}

      <div className="ticket-filter-group">

        <div className="ticket-filter-heading">

          <h4>
            Priority
          </h4>

          <span>
            Ticket urgency level
          </span>

        </div>


        <div className="ticket-filter-grid">

          <div
            className={`ticket-filter-card high ${
              selectedFilter === "High"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("High")
            }
          >

            <span>
              High
            </span>

            <strong>
              {priorityData[0].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>


          <div
            className={`ticket-filter-card medium ${
              selectedFilter === "Medium"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("Medium")
            }
          >

            <span>
              Medium
            </span>

            <strong>
              {priorityData[1].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>


          <div
            className={`ticket-filter-card low ${
              selectedFilter === "Low"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setSelectedFilter("Low")
            }
          >

            <span>
              Low
            </span>

            <strong>
              {priorityData[2].count}
            </strong>

            <small>
              Tickets
            </small>

          </div>

        </div>

      </div>


      {/* Filtered Tickets */}

      {selectedFilter && (

        <div className="category-filtered-ticket-list">

          {filteredTickets.map((ticket) => (

            <div
              className="category-filtered-ticket-card"
              key={ticket.id}
              onClick={() =>
                onTicketClick(ticket)
              }
            >

              <div className="category-ticket-top">

                <div>

                  <strong>
                    #{ticket.id}
                  </strong>

                  <span>
                    {ticket.customer_name}
                  </span>

                </div>

                <span className="ticket-status">
                  {ticket.status}
                </span>

              </div>


              <p className="category-ticket-message">
                {ticket.ticket}
              </p>


              <div className="category-ticket-meta">

                <span>
                  {ticket.category}
                </span>

                <span>
                  {ticket.priority}
                </span>

                <span>
                  {ticket.sentiment}
                </span>

                <span>
                  {ticket.resolution_time_hours}h
                  estimated
                </span>

              </div>

            </div>

          ))}


          {filteredTickets.length === 0 && (

            <div className="category-empty-tickets">

              <h4>
                No tickets found
              </h4>

              <p>
                There are no tickets matching
                this filter.
              </p>

            </div>

          )}

        </div>

      )}

    </section>
  );
}

export default CategoryTicketExplorer;

