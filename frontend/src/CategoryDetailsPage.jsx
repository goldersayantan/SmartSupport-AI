import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import "./CategoryDetailsPage.css";
import CategoryStats from "./components/admin/CategoryStats";
import CategoryAnalytics from "./components/admin/CategoryAnalytics";
import CategoryTicketExplorer from "./components/admin/CategoryTicketExplorer";
import TicketDetails from "./components/admin/TicketDetails";

import {
  getTickets,
  updateTicketStatus
} from "./services/api";

function CategoryDetailsPage() {
  const { category } = useParams();
  const navigate = useNavigate();
  const decodedCategory = decodeURIComponent(category);
  const [tickets, setTickets] = useState([]);
  const [selectedTicket, setSelectedTicket] = useState(null);
  const [selectedFilter, setSelectedFilter] = useState(null);

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const data = await getTickets();
        setTickets(data);
      } catch (error) {
        console.error("Category ticket fetch error:", error);
      }
    };

    fetchTickets();
  }, []);

  const categoryTickets = tickets.filter(
    (ticket) => ticket.category === decodedCategory
  );

  /* -----------------------------
     KPI DATA
  ----------------------------- */

  const totalTickets = categoryTickets.length;

  const openTickets = categoryTickets.filter(
    (ticket) => ticket.status === "Open"
  ).length;

  const inProgressTickets = categoryTickets.filter(
    (ticket) => ticket.status === "In Progress"
  ).length;

  const resolvedTickets = categoryTickets.filter(
    (ticket) => ticket.status === "Resolved"
  ).length;

  const escalatedTickets = categoryTickets.filter(
    (ticket) => ticket.status === "Escalated"
  ).length;

  const averageResolution =
    totalTickets > 0
      ? (
          categoryTickets.reduce(
            (total, ticket) =>
              total +
              Number(ticket.resolution_time_hours || 0),
            0
          ) / totalTickets
        ).toFixed(2)
      : "0.00";

  /* -----------------------------
     CHART DATA
  ----------------------------- */

  const sentimentData = [
    {
      name: "Negative",
      count: categoryTickets.filter(
        (ticket) => ticket.sentiment === "Negative"
      ).length
    },
    {
      name: "Neutral",
      count: categoryTickets.filter(
        (ticket) => ticket.sentiment === "Neutral"
      ).length
    },
    {
      name: "Positive",
      count: categoryTickets.filter(
        (ticket) => ticket.sentiment === "Positive"
      ).length
    }
  ];

  const priorityData = [
    {
      name: "High",
      count: categoryTickets.filter(
        (ticket) => ticket.priority === "High"
      ).length
    },
    {
      name: "Medium",
      count: categoryTickets.filter(
        (ticket) => ticket.priority === "Medium"
      ).length
    },
    {
      name: "Low",
      count: categoryTickets.filter(
        (ticket) => ticket.priority === "Low"
      ).length
    }
  ];

  const statusData = [
    {
      name: "Open",
      count: categoryTickets.filter(
        (ticket) => ticket.status === "Open"
      ).length
    },
    {
      name: "In Progress",
      count: categoryTickets.filter(
        (ticket) => ticket.status === "In Progress"
      ).length
    },
    {
      name: "Resolved",
      count: categoryTickets.filter(
        (ticket) => ticket.status === "Resolved"
      ).length
    },
    {
      name: "Escalated",
      count: categoryTickets.filter(
        (ticket) => ticket.status === "Escalated"
      ).length
    }
  ];

  const resolutionTimeData = categoryTickets.map(
    (ticket) => ({
      name: `#${ticket.id}`,
      hours: Number(
        ticket.resolution_time_hours || 0
      )
    })
  );

  /* -----------------------------
     FILTERED TICKETS
  ----------------------------- */

  const filteredTickets = selectedFilter
    ? categoryTickets.filter(
        (ticket) =>
          ticket.sentiment === selectedFilter ||
          ticket.priority === selectedFilter
      )
    : [];

  /* -----------------------------
     STATUS UPDATE
  ----------------------------- */

  const handleStatusUpdate = async (
    ticketId,
    newStatus
  ) => {
    try {
      await updateTicketStatus(
        ticketId,
        newStatus
      );

      setTickets((currentTickets) =>
        currentTickets.map((ticket) =>
          ticket.id === ticketId
            ? {
                ...ticket,
                status: newStatus
              }
            : ticket
        )
      );

      setSelectedTicket((currentTicket) =>
        currentTicket?.id === ticketId
          ? {
              ...currentTicket,
              status: newStatus
            }
          : currentTicket
      );
    } catch (error) {
      console.error(
        "Category status update error:",
        error
      );
    }
  };

  return (
    <div className="app">

      <header className="header">
        <div className="brand">
          <div className="logo">S</div>

          <div>
            <h1>SmartSupport AI</h1>
            <p>Category Analytics</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          Admin Panel
        </div>
      </header>

      <main className="dashboard">

        <button
          className="category-back-button"
          onClick={() => navigate("/admin")}
        >
          ← Back to Admin Dashboard
        </button>

        <section className="category-page-header">
          <div>
            <span className="category-page-label">
              Ticket Category
            </span>

            <h2>{decodedCategory}</h2>

            <p>
              Analyze tickets, sentiment, priority,
              status, and estimated resolution time.
            </p>
          </div>
        </section>

        <CategoryStats
          totalTickets={totalTickets}
          openTickets={openTickets}
          inProgressTickets={inProgressTickets}
          resolvedTickets={resolvedTickets}
          escalatedTickets={escalatedTickets}
          averageResolution={averageResolution}
        />

        <CategoryAnalytics
          category={decodedCategory}
          sentimentData={sentimentData}
          priorityData={priorityData}
          statusData={statusData}
          resolutionTimeData={resolutionTimeData}
          onFilterSelect={setSelectedFilter}
        />

        <CategoryTicketExplorer
          sentimentData={sentimentData}
          priorityData={priorityData}
          selectedFilter={selectedFilter}
          setSelectedFilter={setSelectedFilter}
          filteredTickets={filteredTickets}
          onTicketClick={setSelectedTicket}
        />

        {selectedTicket && (
          <TicketDetails
            ticket={selectedTicket}
            onBack={() => setSelectedTicket(null)}
            updateStatus={handleStatusUpdate}
          />
        )}

      </main>

      <footer>
        <p>SmartSupport AI • Category Analytics</p>
      </footer>

    </div>
  );
}

export default CategoryDetailsPage;

