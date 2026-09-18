import { useNavigate } from "react-router-dom";
import "./CategoryExplorer.css";

function CategoryExplorer({
  tickets,
  selectedCategory,
  setSelectedCategory
}) {
  const navigate = useNavigate();

  const categories = [
    ...new Set(
      tickets.map((ticket) => ticket.category)
    )
  ];

  const openCategory = (category) => {
    setSelectedCategory(category);

    navigate(
      `/admin/category/${encodeURIComponent(category)}`
    );
  };

  return (
    <section className="category-section">

      <div className="section-heading">
        <div>
          <h2>Ticket Categories</h2>
          <p>
            Select a category to explore its analytics.
          </p>
        </div>
      </div>

      <div className="category-grid">

        {categories.map((category) => {

          const categoryCount = tickets.filter(
            (ticket) => ticket.category === category
          ).length;

          return (
            <div
              className={`category-card ${
                selectedCategory === category
                  ? "selected"
                  : ""
              }`}
              key={category}
              onClick={() => openCategory(category)}
            >

              <h3>{category}</h3>

              <strong>{categoryCount}</strong>

              <span>Tickets</span>

            </div>
          );
        })}

      </div>

    </section>
  );
}

export default CategoryExplorer;