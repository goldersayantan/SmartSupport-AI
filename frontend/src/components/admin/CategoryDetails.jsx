import "./CategoryDetails.css";

function CategoryDetails({
  tickets,
  selectedCategory,
  selectedFilter,
  setSelectedFilter,
  setSelectedCategory
}) {
  if (!selectedCategory) {
    return null;
  }

  const categoryTickets = tickets.filter(
    (ticket) => ticket.category === selectedCategory
  );

  const negative = categoryTickets.filter(
    (ticket) => ticket.sentiment === "Negative"
  ).length;

  const neutral = categoryTickets.filter(
    (ticket) => ticket.sentiment === "Neutral"
  ).length;

  const positive = categoryTickets.filter(
    (ticket) => ticket.sentiment === "Positive"
  ).length;

  const high = categoryTickets.filter(
    (ticket) => ticket.priority === "High"
  ).length;

  const medium = categoryTickets.filter(
    (ticket) => ticket.priority === "Medium"
  ).length;

  const low = categoryTickets.filter(
    (ticket) => ticket.priority === "Low"
  ).length;

  return (
    <section className="category-details">

      <div className="selected-category-header">
        <div>
          <h2>{selectedCategory}</h2>

          <p>
            AI analysis for this ticket category
          </p>
        </div>

        <button
          className="clear-category"
          onClick={() => {
            setSelectedCategory(null);
            setSelectedFilter(null);
          }}
        >
          View All Categories
        </button>
      </div>

      <div className="category-analytics">

        {/* Sentiment */}

        <div className="analytics-card">
          <h3>Sentiment</h3>

          <div className="analytics-boxes">

            <div
              className={`analytics-box negative ${
                selectedFilter === "Negative" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("Negative")}
            >
              <span>Negative</span>
              <strong>{negative}</strong>
            </div>

            <div
              className={`analytics-box neutral ${
                selectedFilter === "Neutral" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("Neutral")}
            >
              <span>Neutral</span>
              <strong>{neutral}</strong>
            </div>

            <div
              className={`analytics-box positive ${
                selectedFilter === "Positive" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("Positive")}
            >
              <span>Positive</span>
              <strong>{positive}</strong>
            </div>

          </div>
        </div>

        {/* Priority */}

        <div className="analytics-card">
          <h3>Priority</h3>

          <div className="analytics-boxes">

            <div
              className={`analytics-box high ${
                selectedFilter === "High" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("High")}
            >
              <span>High</span>
              <strong>{high}</strong>
            </div>

            <div
              className={`analytics-box medium ${
                selectedFilter === "Medium" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("Medium")}
            >
              <span>Medium</span>
              <strong>{medium}</strong>
            </div>

            <div
              className={`analytics-box low ${
                selectedFilter === "Low" ? "active" : ""
              }`}
              onClick={() => setSelectedFilter("Low")}
            >
              <span>Low</span>
              <strong>{low}</strong>
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}

export default CategoryDetails;