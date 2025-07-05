import React from "react";
import RegisterForm from "../components/Auth/RegisterForm";
import { useNavigate } from "react-router-dom";

export default function RegisterPage() {
  const navigate = useNavigate();

  function handleRegister(data) {
    // Здесь обычно отправляется регистрационная форма на сервер
    // После успешной регистрации — переход на ввод кода
    navigate("/code");
  }

  function handleSwitchToLogin() {
    navigate("/login");
  }

  return (
    <RegisterForm onSubmit={handleRegister} switchToLogin={handleSwitchToLogin} />
  );
}