import React, { useState } from "react";
import LoginForm from "../components/Auth/LoginForm";
import RegisterForm from "../components/Auth/RegisterForm";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [mode, setMode] = useState("login"); // "login" | "register"
  const navigate = useNavigate();

  function handleLogin(phone) {
    // Здесь обычно делается запрос к серверу и обработка ошибки/успеха
    // Для примера сразу переходим на ввод кода
    navigate("/code");
  }

  function handleRegister(data) {
    // Аналогично — обычно отправка данных на сервер
    navigate("/code");
  }

  return (
    <div>
      {mode === "login" ? (
        <LoginForm onSubmit={handleLogin} switchToRegister={() => setMode("register")} />
      ) : (
        <RegisterForm onSubmit={handleRegister} switchToLogin={() => setMode("login")} />
      )}
    </div>
  );
}