import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import AuthTabs from "../features/auth/components/AuthTabs";
import LoginPage from "../pages/login-page/LoginPage";

function App() {
  return (
    <>
      <LoginPage/>
    </>
  );
}

export default App;