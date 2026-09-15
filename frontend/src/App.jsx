import { BrowserRouter, Routes, Route } from "react-router-dom";

import CustomerPage from "./CustomerPage";
import AdminPage from "./AdminPage";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<CustomerPage />}
        />

        <Route
          path="/admin"
          element={<AdminPage />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;