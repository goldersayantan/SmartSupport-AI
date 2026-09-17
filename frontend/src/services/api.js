const API_URL = "http://127.0.0.1:8000";

export async function getTickets() {
  const response = await fetch(
    `${API_URL}/tickets`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return await response.json();
}

export async function updateTicketStatus(
  ticketId,
  newStatus
) {
  const response = await fetch(
    `${API_URL}/tickets/${ticketId}/status`,
    {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        status: newStatus,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to update status");
  }

  return await response.json();
}