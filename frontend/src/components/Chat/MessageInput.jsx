import React from "react";

export default function MessageInput({ value, onChange, onSend }) {
  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  }

  return (
    <div style={styles.inputBox}>
      <textarea
        style={styles.textarea}
        placeholder="Сообщение..."
        value={value}
        onChange={e => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        rows={1}
      />
      <button style={styles.button} onClick={onSend}>
        Отправить
      </button>
    </div>
  );
}

const styles = {
  inputBox: {
    display: "flex",
    alignItems: "center",
    padding: "12px",
    background: "#f9fcff",
    gap: "10px",
    borderTop: "1px solid #dde9f0",
  },
  textarea: {
    flex: 1,
    padding: "10px",
    borderRadius: "6px",
    border: "1px solid #c2e3fa",
    fontSize: "16px",
    outline: "none",
    resize: "none",
    minHeight: "40px",
    maxHeight: "80px",
  },
  button: {
    background: "#47a2f3",
    color: "#fff",
    border: "none",
    padding: "10px 18px",
    borderRadius: "6px",
    fontWeight: "bold",
    cursor: "pointer",
    fontSize: "16px",
  },
};