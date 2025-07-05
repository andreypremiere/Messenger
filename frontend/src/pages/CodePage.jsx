import React, { useState } from "react";
import CodeInput from "../components/Auth/CodeInput";
import { useNavigate } from "react-router-dom";

export default function CodePage() {
  const [error, setError] = useState("");
  const navigate = useNavigate();

  function handleComplete(code) {
    // Тут может быть валидация кода через сервер
    if (code === "123456") {
      navigate("/chat");
    } else {
      setError("Неверный код");
    }
  }

  return (
    <div>
      <CodeInput length={6} onComplete={handleComplete} />
      {error && <div style={{ color: "red", textAlign: "center" }}>{error}</div>}
    </div>
  );
}