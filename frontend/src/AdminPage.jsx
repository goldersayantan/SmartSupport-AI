import { useEffect, useState } from "react";
import "./App.css";

import DashboardStats from "./components/admin/DashboardStats";
import CategoryExplorer from "./components/admin/CategoryExplorer";

import {
  getTickets
} from "./services/api";

function AdminPage() {
  const [tickets, setTickets] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  const fetchTickets = async () => {
    try {
      const data = await getTickets();
      setTickets(data);
    } catch (err) {
      console.log("Ticket fetch error:", err);
    }
  };

  useEffect(() => {
    fetchTickets();
  }, []);

  const totalTickets = tickets.length;

  const openTickets = tickets.filter(
    (ticket) => ticket.status === "Open"
  ).length;

  const inProgressTickets = tickets.filter(
    (ticket) => ticket.status === "In Progress"
  ).length;

  const resolvedTickets = tickets.filter(
    (ticket) => ticket.status === "Resolved"
  ).length;

  const escalatedTickets = tickets.filter(
    (ticket) => ticket.status === "Escalated"
  ).length;

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

        <DashboardStats
          totalTickets={totalTickets}
          openTickets={openTickets}
          inProgressTickets={inProgressTickets}
          resolvedTickets={resolvedTickets}
          escalatedTickets={escalatedTickets}
        />

        <CategoryExplorer
          tickets={tickets}
          selectedCategory={selectedCategory}
          setSelectedCategory={setSelectedCategory}
        />

      </main>

      <footer>
        <p>SmartSupport AI • Admin Portal</p>
      </footer>

    </div>
  );
}

export default AdminPage;
