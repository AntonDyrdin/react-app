import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./reset-user-agent.css";

const container = document.getElementById("root")!;
createRoot(container).render(<App />);
