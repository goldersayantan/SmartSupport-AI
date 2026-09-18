import { useEffect, useState } from "react";

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
  // Previous Tickets State
  // --------------------------------

  const [previousTickets, setPreviousTickets] = useState([]);
  const [ticketsLoading, setTicketsLoading] = useState(false);
  const [ticketsError, setTicketsError] = useState("");


  // --------------------------------
  // Load Customer Tickets
  // --------------------------------

  const loadPreviousTickets = async () => {

    const token = localStorage.getItem("access_token");

    if (!token) {
      return;
    }

    setTicketsLoading(true);
    setTicketsError("");

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/tickets/my-tickets",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
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
          "Unable to load your previous tickets."
        );
      }

      const data = await response.json();
      setPreviousTickets(data);
    } catch (err) {
      setTicketsError(err.message);
      console.error(
        "Previous tickets error:",
        err
      );
    } finally {
      setTicketsLoading(false);
    }
  };


  // Load tickets whenever customer logs in
  useEffect(() => {
    if (user) {
      loadPreviousTickets();
    }

  }, [user]);


  // --------------------------------
  // Analyze Ticket
  // --------------------------------

  const analyzeTicket = async () => {
    if (!ticket.trim()) {
      setError(
        "Please enter a support ticket."
      );
      return;
    }

    const token = localStorage.getItem(
      "access_token"
    );

    if (!token) {
      setError(
        "Please sign in before submitting a ticket."
      );
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
              customerName ||
              user?.name ||
              "Anonymous",
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

      // Refresh previous tickets
      await loadPreviousTickets();
    } catch (err) {
      setError(err.message);
      console.error(
        "Error:",
        err
      );

    } finally {
      setLoading(false);
    }
  };


  // --------------------------------
  // Authentication Screen
  // --------------------------------

  if (!user) {
    return (
      <CustomerAuth
        onLogin={handleLogin}
      />
    );
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

        {/* Welcome */}
        <section className="customer-welcome">
          <div>
            <span className="welcome-label">CUSTOMER PORTAL</span>
            <h2>Welcome, {user.name}</h2>
            <p>
              Submit a support request and let
              SmartSupport AI analyze it automatically.
            </p>
          </div>
        </section>


        {/* Ticket Form */}
        <TicketForm
          ticket={ticket}
          setTicket={setTicket}
          customerName={customerName}
          setCustomerName={setCustomerName}
          loading={loading}
          error={error}
          onAnalyze={analyzeTicket}
        />


        {/* Example Tickets */}
        <ExampleTickets
          onSelect={setTicket}
        />


        {/* Current Ticket Analysis */}
        {result && (
          <TicketAnalysis
            result={result}
          />
        )}


        {/* --------------------------------
            Previous Tickets
        -------------------------------- */}

        <section className="previous-tickets">
          <div className="previous-tickets-header">
            <div>
              <span className="previous-tickets-label">YOUR ACTIVITY</span>
              <h3>Previous Tickets</h3>
            </div>
          </div>

          {/* Loading */}

          {ticketsLoading && (
            <div className="previous-tickets-message">
              Loading your previous tickets...
            </div>
          )}

          {/* Error */}

          {!ticketsLoading && ticketsError && (
            <div className="previous-tickets-message previous-tickets-error">
              {ticketsError}
            </div>
          )}

          {/* Empty State */}

          {!ticketsLoading &&
            !ticketsError &&
            previousTickets.length === 0 && (
              <div className="previous-tickets-message">
                <h4>No previous tickets yet</h4>
                <p>Your submitted support tickets will appear here.</p>
              </div>
            )}


          {/* Ticket Cards */}

          {!ticketsLoading &&
            previousTickets.length > 0 && (
              <div className="previous-tickets-list">
                {previousTickets.map((previousTicket) => (
                  <div className="previous-ticket-card" key={previousTicket.id}>
                    <p className="previous-ticket-description">{previousTicket.ticket}</p>

                    <div className="previous-ticket-meta">
                      <div className="previous-ticket-category">
                        <span>Category</span>
                        <strong>{previousTicket.category}</strong>
                      </div>

                      <div className="previous-ticket-status">
                        <span>Status</span>
                        <strong
                          className={`ticket-status-badge status-${previousTicket.status
                            ?.toLowerCase()
                            .replace(/\s+/g, "-")}`}
                        >
                          {previousTicket.status}
                        </strong>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
        </section>
      </main>

      <footer className="customer-footer">
        <p>SmartSupport AI • Intelligent Customer Support</p>
      </footer>
    </div>
  );
}

export default CustomerPage;

