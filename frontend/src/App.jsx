import { BrowserRouter, Routes, Route } from "react-router-dom";

import CustomerPage from "./CustomerPage";
import AdminPage from "./AdminPage";
import CategoryDetailsPage from "./CategoryDetailsPage";

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

        <Route
          path="/admin/category/:category"
          element={<CategoryDetailsPage />}
        />

      </Routes>


    </BrowserRouter>
  );
}

export default App;