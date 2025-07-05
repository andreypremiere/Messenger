import React from "react";

export default function ChatWindow({ chat, messages, onSendMessage }) {
  const [input, setInput] = React.useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (input.trim()) {
      onSendMessage(input);
      setInput("");
    }
  }

  return (
    <div style={styles.window}>
      <div style={styles.header}>
        <div style={styles.headerLeft}>
          <span style={{ ...styles.circle, background: chat.color }} />
          <div>
            <div style={styles.chatTitle}>{chat.title}</div>
            <div style={styles.onlineRow}>
              <span style={styles.statusDot} /> <span style={styles.statusText}>online</span>
            </div>
          </div>
        </div>
        <div style={styles.headerActions}>
          <button style={styles.iconBtn} title="Позвонить">&#128222;</button>
          <button style={styles.iconBtn} title="Видеозвонок">&#128249;</button>
          <button style={styles.iconBtn} title="Ещё">&#8942;</button>
        </div>
      </div>
      <div style={styles.messages}>
        {messages.length === 0 && <div style={styles.empty}>Нет сообщений</div>}
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              ...styles.message,
              alignSelf: msg.isMe ? "flex-end" : "flex-start",
              background: msg.isMe ? "#eaf6fb" : "#fff",
              color: "#222",
            }}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <form style={styles.form} onSubmit={handleSubmit}>
        <input
          style={styles.input}
          placeholder="Сообщение"
          value={input}
          onChange={e => setInput(e.target.value)}
        />
        <button style={styles.voiceBtn} type="button" tabIndex={-1} title="Голосовое сообщение">
          <span role="img" aria-label="mic">&#127908;</span>
        </button>
      </form>
    </div>
  );
}

const styles = {
  window: {
    display: "flex",
    flexDirection: "column",
    height: "100%",
    background: "#b7e1fa",
    borderRadius: "0px",
    overflow: "hidden",
    minWidth: 0,
  },
  header: {
    padding: "10px 24px 10px 20px",
    background: "#fff",
    borderBottom: "1px solid #dde9f0",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    minHeight: "64px",
  },
  headerLeft: {
    display: "flex",
    alignItems: "center",
    gap: "14px",
  },
  circle: {
    width: "38px",
    height: "38px",
    borderRadius: "50%",
    display: "inline-block",
    border: "2px solid #dde9f0",
  },
  chatTitle: {
    fontWeight: "bold",
    fontSize: "18px",
    color: "#222",
    marginBottom: "2px",
    marginTop: "2px",
  },
  onlineRow: {
    display: "flex",
    alignItems: "center",
    gap: "6px",
    fontSize: "13px",
    color: "#62cf64",
  },
  statusDot: {
    display: "inline-block",
    width: "8px",
    height: "8px",
    borderRadius: "50%",
    background: "#62cf64",
  },
  statusText: {
    color: "#62cf64",
  },
  headerActions: {
    display: "flex",
    gap: "8px",
    alignItems: "center",
  },
  iconBtn: {
    background: "#f6fafd",
    border: "none",
    borderRadius: "7px",
    fontSize: "20px",
    color: "#7d8fa6",
    padding: "7px",
    cursor: "pointer",
    marginLeft: "2px",
    transition: "background 0.15s",
  },
  messages: {
    flex: 1,
    padding: "30px 32px",
    display: "flex",
    flexDirection: "column",
    gap: "14px",
    overflowY: "auto",
    background: "#b7e1fa",
    minHeight: 0,
  },
  message: {
    maxWidth: "60%",
    padding: "10px 16px",
    borderRadius: "10px",
    fontSize: "15px",
    marginBottom: "4px",
    wordBreak: "break-word",
    boxShadow: "0 1px 3px #0001",
    background: "#fff",
    color: "#252525",
  },
  empty: {
    color: "#aaa",
    textAlign: "center",
    marginTop: "30px",
  },
  form: {
    display: "flex",
    alignItems: "center",
    padding: "14px 18px",
    background: "#fff",
    gap: "10px",
    borderTop: "1px solid #dde9f0",
  },
  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #c2e3fa",
    fontSize: "16px",
    outline: "none",
    background: "#f6fafd",
  },
  voiceBtn: {
    background: "#eaf6fb",
    color: "#47a2f3",
    border: "none",
    padding: "8px 12px",
    borderRadius: "8px",
    fontWeight: "bold",
    cursor: "pointer",
    fontSize: "20px",
    marginLeft: "5px",
    transition: "background 0.18s",
  },
};