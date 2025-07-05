import React, { useState } from "react";

export default function RegisterForm({ onSubmit, switchToLogin }) {
  const [name, setName] = useState("");
  const [emailOrPhone, setEmailOrPhone] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit({ name, emailOrPhone, password });
  }

  return (
    <div style={styles.container}>
      <form style={styles.form} onSubmit={handleSubmit}>
        <div style={styles.tabs}>
          <button type="button" style={styles.tab} onClick={switchToLogin}>
            Вход
          </button>
          <button type="button" style={{ ...styles.tab, ...styles.activeTab }}>
            Регистрация
          </button>
        </div>
        <input
          style={styles.input}
          type="text"
          placeholder="Имя (никнейм)"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <input
          style={styles.input}
          type="text"
          placeholder="Эл.почта или телефон"
          value={emailOrPhone}
          onChange={e => setEmailOrPhone(e.target.value)}
        />
        <input
          style={styles.input}
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <button style={styles.button} type="submit">
          Получить код
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "80vh",
    background: "#eaf6fb",
  },
  form: {
    padding: "32px",
    borderRadius: "8px",
    background: "#fff",
    boxShadow: "0 2px 10px #0001",
    display: "flex",
    flexDirection: "column",
    minWidth: "320px",
  },
  tabs: {
    display: "flex",
    marginBottom: "16px",
  },
  tab: {
    flex: 1,
    padding: "8px",
    background: "none",
    border: "none",
    borderBottom: "2px solid transparent",
    fontSize: "18px",
    cursor: "pointer",
  },
  activeTab: {
    borderBottom: "2px solid #47a2f3",
    color: "#47a2f3",
    fontWeight: "bold",
  },
  input: {
    marginBottom: "16px",
    padding: "10px",
    borderRadius: "4px",
    border: "1px solid #c2e3fa",
    fontSize: "16px",
  },
  button: {
    background: "#47a2f3",
    color: "#fff",
    padding: "10px",
    border: "none",
    borderRadius: "4px",
    fontWeight: "bold",
    cursor: "pointer",
    fontSize: "16px",
  },
};