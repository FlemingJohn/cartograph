import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";
import "./styles/theme.css";
import "./styles/layout.css";
import "./styles/controls.css";
import "./styles/navigation.css";
import "./styles/findings.css";
import "./styles/details.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
