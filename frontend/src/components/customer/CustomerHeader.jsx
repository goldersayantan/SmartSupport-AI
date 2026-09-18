import "./CustomerHeader.css";

function CustomerHeader({ user, onLogout }) {
  return (
    <header className="customer-header">

      <div className="customer-brand">
        <div className="customer-logo">S</div>
        <div>
          <h1>SmartSupport AI</h1>
          <p>AI-powered customer support intelligence</p>
        </div>
      </div>

      <div className="customer-header-right">
        <div className="system-status">
          <span className="system-status-dot"></span>
          AI System Online
        </div>

        <div className="customer-profile">
          <div className="customer-avatar">
            {user?.name?.charAt(0)?.toUpperCase()}
          </div>

          <div className="customer-profile-info">
            <strong>{user?.name}</strong>
            <span>{user?.email}</span>
          </div>
        </div>

        <button type="button" className="customer-logout" onClick={onLogout}>Logout</button>
      </div>
    </header>
  );
}

export default CustomerHeader;

