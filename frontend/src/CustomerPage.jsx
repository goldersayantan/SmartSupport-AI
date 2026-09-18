import { useState } from "react";

import "./App.css";
import "./CustomerPage.css";

import CustomerAuth from "./components/customer/CustomerAuth";
import CustomerHeader from "./components/customer/CustomerHeader";
import TicketForm from "./components/customer/TicketForm";
import ExampleTickets from "./components/customer/ExampleTickets";
import TicketAnalysis from "./components/customer/TicketAnalysis";

function CustomerPage() {
  // --------------------------------
  // Authentication
  // --------------------------------

  const savedUser = localStorage.getItem("user");

  const [user, setUser] = useState(
    savedUser ? JSON.parse(savedUser) : null
  );

  const handleLogin = (loggedInUser) => {
    setUser(loggedInUser);
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user");

    setUser(null);
  };

  // --------------------------------
  // Ticket State
  // --------------------------------

  const [ticket, setTicket] = useState("");
  const [customerName, setCustomerName] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // --------------------------------
  // Analyze Ticket
  // --------------------------------

  const analyzeTicket = async () => {
    if (!ticket.trim()) {
      setError("Please enter a support ticket.");
      return;
    }

    const token = localStorage.getItem("access_token");

    if (!token) {
      setError("Please sign in before submitting a ticket.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            ticket,
            customer_name:
              customerName || user?.name || "Anonymous",
          }),
        }
      );

      if (response.status === 401) {
        handleLogout();

        throw new Error(
          "Your session has expired. Please sign in again."
        );
      }

      if (!response.ok) {
        const errorData = await response.json();

        throw new Error(
          errorData.detail ||
            errorData.error ||
            "Unable to analyze ticket."
        );
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      setError(err.message);
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  // --------------------------------
  // Authentication Screen
  // --------------------------------

  if (!user) {
    return <CustomerAuth onLogin={handleLogin} />;
  }

  // --------------------------------
  // Customer Portal
  // --------------------------------

  return (
    <div className="customer-page">
      <CustomerHeader
        user={user}
        onLogout={handleLogout}
      />

      <main className="customer-dashboard">

        <section className="customer-welcome">
          <div>
            <span className="welcome-label">
              CUSTOMER PORTAL
            </span>

            <h2>
              Welcome, {user.name}
            </h2>

            <p>
              Submit a support request and let SmartSupport AI
              analyze it automatically.
            </p>
          </div>
        </section>

        <TicketForm
          ticket={ticket}
          setTicket={setTicket}
          customerName={customerName}
          setCustomerName={setCustomerName}
          loading={loading}
          error={error}
          onAnalyze={analyzeTicket}
        />

        <ExampleTickets
          onSelect={setTicket}
        />

        {result && (
          <TicketAnalysis result={result} />
        )}

      </main>

      <footer className="customer-footer">
        <p>
          SmartSupport AI • Intelligent Customer Support
        </p>
      </footer>
    </div>
  );
}

export default CustomerPage;

