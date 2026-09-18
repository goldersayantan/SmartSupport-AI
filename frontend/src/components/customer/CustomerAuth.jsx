import { useState } from "react";
import { useNavigate } from "react-router-dom";

import "./CustomerAuth.css";

function CustomerAuth({ onLogin }) {
  const navigate = useNavigate();
  const [mode, setMode] = useState("login");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setMessage("");
    setLoading(true);

    try {
      if (mode === "signup") {
        const response = await fetch(
          "http://127.0.0.1:8000/auth/signup",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              name,
              email,
              password,
            }),
          }
        );

        const data = await response.json();

        if (!response.ok || data.error) {
          throw new Error(
            data.error || "Unable to create account"
          );
        }

        setMessage(
          "Account created successfully. Please sign in."
        );

        setMode("login");
        setName("");
        setPassword("");
      } else {
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

        if (!response.ok || data.error) {
          throw new Error(
            data.error || "Invalid email or password"
          );
        }

        localStorage.setItem(
          "access_token",
          data.access_token
        );

        localStorage.setItem(
          "user",
          JSON.stringify(data.user)
        );

        onLogin(data.user);
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const switchMode = (nextMode) => {
    setMode(nextMode);
    setError("");
    setMessage("");
  };

  return (
    <div className="customer-auth-page">
      <div className="customer-auth-left">
        <div className="auth-brand">
          <div className="auth-logo">S</div>
          <span>SmartSupport AI</span>
        </div>

        <div className="auth-hero">
          <span className="auth-eyebrow">AI-POWERED SUPPORT</span>
          <h1>Smarter support.<br />Faster solutions.</h1>
          <p>
            Submit your support request and let SmartSupport AI
            automatically understand, prioritize, and analyze
            your issue.
          </p>

          <div className="auth-features">
            <div className="auth-feature">
              <div>✦</div>
              <div>
                <strong>AI-powered analysis</strong>
                <span>Automatic category, priority and sentiment detection.</span>
              </div>
            </div>

            <div className="auth-feature">
              <div>◷</div>
              <div>
                <strong>Resolution estimation</strong>
                <span>Get an estimated time for handling your request.</span>
              </div>
            </div>

            <div className="auth-feature">
              <div>✓</div>
              <div>
                <strong>Secure support portal</strong>
                <span>Your tickets are connected to your account.</span>
              </div>
            </div>
          </div>
        </div>
        <div className="auth-left-footer">Intelligent Customer Support</div>
      </div>

      <div className="customer-auth-right">
        <div className="auth-card">

          {/* Portal Toggle */}

          <div className="portal-toggle">
            <button type="button" className="portal-toggle-active">Customer</button>
            <button type="button" onClick={() => navigate("/admin")}>Admin</button>
          </div>

          <div className="auth-card-header">
            <div className="mobile-auth-logo">S</div>
            <span className="auth-card-label">CUSTOMER PORTAL</span>
            <h2>
              {mode === "login"
                ? "Welcome back"
                : "Create your account"}
            </h2>

            <p>
              {mode === "login"
                ? "Sign in to manage your support requests."
                : "Create an account to get started."}
            </p>
          </div>

          <div className="auth-tabs">
            <button
              type="button"
              className={
                mode === "login"
                  ? "active"
                  : ""
              }
              onClick={() => switchMode("login")}
            >
              Sign In
            </button>

            <button
              type="button"
              className={
                mode === "signup"
                  ? "active"
                  : ""
              }
              onClick={() => switchMode("signup")}
            >
              Sign Up
            </button>
          </div>

          {error && (
            <div className="auth-message auth-error">
              <span>!</span>
              {error}
            </div>
          )}

          {message && (
            <div className="auth-message auth-success">
              <span>✓</span>
              {message}
            </div>
          )}

          <form className="auth-form" onSubmit={handleSubmit}>
            {mode === "signup" && (
              <div className="auth-field">
                <label>Full Name</label>
                <input
                  type="text"
                  value={name}
                  onChange={(event) =>
                    setName(event.target.value)
                  }
                  placeholder="Enter your name"
                  required
                />
              </div>
            )}

            <div className="auth-field">
              <label>Email Address</label>
              <input
                type="email"
                value={email}
                onChange={(event) =>
                  setEmail(event.target.value)
                }
                placeholder="you@example.com"
                required
              />
            </div>

            <div className="auth-field">
              <label>Password</label>
              <input
                type="password"
                value={password}
                onChange={(event) =>
                  setPassword(event.target.value)
                }
                placeholder="Enter your password"
                required
              />
            </div>

            <button type="submit" className="auth-submit" disabled={loading}>
              {loading ? (
                <>
                  <span className="auth-spinner"></span>
                  Please wait...
                </>
              ) : mode === "login" ? (
                <>
                  Sign In
                  <span>→</span>
                </>
              ) : (
                <>
                  Create Account
                  <span>→</span>
                </>
              )}

            </button>
          </form>

          <p className="auth-switch">
            {mode === "login"
              ? "Don't have an account?"
              : "Already have an account?"}

            <button
              type="button"
              onClick={() =>
                switchMode(
                  mode === "login"
                    ? "signup"
                    : "login"
                )
              }
            >
              {mode === "login"
                ? "Create one"
                : "Sign in"}
            </button>
          </p>

          <div className="auth-security">
            <span>🔒</span>
            Your account information is securely protected.
          </div>
        </div>
      </div>
    </div>
  );
}

export default CustomerAuth;
