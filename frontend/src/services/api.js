const API_URL = "http://127.0.0.1:8000";

// --------------------------------
// Get all tickets
// Admin only
// --------------------------------

export async function getTickets() {
  const token = localStorage.getItem("access_token");

  const response = await fetch(
    `${API_URL}/tickets`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  // JWT expired or invalid
  if (response.status === 401) {
    throw new Error("SESSION_EXPIRED");
  }

  if (!response.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return await response.json();
}


// --------------------------------
// Update ticket status
// Admin only
// --------------------------------

export async function updateTicketStatus(
  ticketId,
  newStatus
) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(
    `${API_URL}/tickets/${ticketId}/status`,
    {
      method: "PATCH",

      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },

      body: JSON.stringify({
        status: newStatus,
      }),
    }
  );

  // JWT expired or invalid
  if (response.status === 401) {
    throw new Error("SESSION_EXPIRED");
  }

  if (!response.ok) {
    throw new Error("Failed to update status");
  }

  return await response.json();
}

