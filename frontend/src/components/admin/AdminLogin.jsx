import { useState } from "react";
import { useNavigate } from "react-router-dom";

import "./AdminLogin.css";

function AdminLogin({ onLogin }) {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();

    if (!email.trim() || !password) {
      setError("Please enter your email and password.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email,
            password,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.error ||
            "Unable to sign in."
        );
      }

      if (data.error) {
        throw new Error(data.error);
      }

      // Make sure this account is actually an admin
      if (data.user?.role !== "admin") {
        throw new Error(
          "You do not have permission to access the admin panel."
        );
      }

      // Save authentication information
      localStorage.setItem(
        "access_token",
        data.access_token
      );

      localStorage.setItem(
        "user",
        JSON.stringify(data.user)
      );

      // Tell AdminPage that login succeeded
      onLogin(data.user);

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="admin-login-page">

      {/* --------------------------------
          Left Branding Section
      -------------------------------- */}

      <section className="admin-login-left">
        <div className="admin-brand">
          <div className="admin-logo">S</div>
          <span>SmartSupport AI</span>
        </div>

        <div className="admin-login-hero">
          <span className="admin-eyebrow">ADMINISTRATION</span>
          <h1>
            Manage support
            <span> intelligently.</span>
          </h1>

          <p>
            Access your SmartSupport AI administration
            dashboard to monitor tickets, analyze support
            activity, and manage customer requests.
          </p>

          <div className="admin-features">
            <div className="admin-feature">
              <div className="admin-feature-icon">✓</div>
              <div>
                <strong>AI-powered insights</strong>
                <span>Monitor automated ticket analysis.</span>
              </div>
            </div>

            <div className="admin-feature">
              <div className="admin-feature-icon">✓</div>
              <div>
                <strong>Ticket management</strong>
                <span>Review and manage customer requests.</span>
              </div>
            </div>

            <div className="admin-feature">
              <div className="admin-feature-icon">✓</div>
              <div>
                <strong>Secure access</strong>
                <span>Protected administrator-only access.</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* --------------------------------
          Login Section
      -------------------------------- */}

      <section className="admin-login-right">
        <div className="admin-login-card">

          {/* --------------------------------
              Customer / Admin Toggle
          -------------------------------- */}

          <div className="portal-toggle">
            <button type="button" onClick={() => navigate("/")}>Customer</button>
            <button type="button" className="portal-toggle-active">Admin</button>
          </div>

          {/* --------------------------------
              Card Header
          -------------------------------- */}

          <div className="admin-card-header">
            <div className="admin-lock-icon">🔐</div>
            <div>
              <span className="admin-card-label">SECURE ACCESS</span>
              <h2>Admin Sign In</h2>
              <p>Sign in to access the administration dashboard.</p>
            </div>
          </div>

          {/* --------------------------------
              Error
          -------------------------------- */}

          {error && (
            <div className="admin-login-error">
              <span>!</span>
              {error}
            </div>
          )}

          {/* --------------------------------
              Login Form
          -------------------------------- */}

          <form className="admin-login-form" onSubmit={handleLogin}>
            <div className="admin-field">
              <label htmlFor="admin-email">Email address</label>
              <input
                id="admin-email"
                type="email"
                placeholder="admin@smartsupport.ai"
                value={email}
                onChange={(event) =>
                  setEmail(event.target.value)
                }
                autoComplete="email"
                disabled={loading}
              />
            </div>

            <div className="admin-field">
              <label htmlFor="admin-password">Password</label>
              <input
                id="admin-password"
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={(event) =>
                  setPassword(event.target.value)
                }
                autoComplete="current-password"
                disabled={loading}
              />
            </div>

            <button type="submit" className="admin-login-button" disabled={loading}>
              {loading ? (
                <>
                  <span className="admin-spinner"></span>
                  Signing in...
                </>
              ) : (
                <>
                  Sign In
                  <span className="admin-arrow">
                    →
                  </span>
                </>
              )}
            </button>
          </form>

          {/* --------------------------------
              Security Note
          -------------------------------- */}

          <div className="admin-security-note">
            <span className="admin-security-icon">✓</span>
            <div>
              <strong>Administrator access only</strong>
              <p>
                This area is restricted to authorized
                SmartSupport administrators.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default AdminLogin;

