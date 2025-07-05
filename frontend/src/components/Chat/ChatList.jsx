import React from "react";

export default function ChatList({ chats, selectedId, onSelect }) {
  return (
    <div style={styles.list}>
      <div style={styles.searchBox}>
        <input
          style={styles.search}
          placeholder="Поиск"
        />
        <span style={styles.searchIcon}>&#128269;</span>
      </div>
      <div style={styles.chats}>
        {chats.length === 0 && <div style={styles.empty}>Нет чатов</div>}
        {chats.map(chat => (
          <div
            key={chat.id}
            style={{
              ...styles.item,
              background: chat.id === selectedId ? "#eaf6fb" : "transparent",
            }}
            onClick={() => onSelect(chat.id)}
          >
            <span style={{ ...styles.circle, background: chat.color }} />
            <div style={styles.chatInfo}>
              <div style={styles.titleRow}>
                <span style={styles.title}>{chat.title}</span>
              </div>
              <span style={styles.lastMsg}>
                {chat.lastMessage ? (
                  <>
                    <span style={styles.lastMsgPrefix}>Вы: </span>
                    <span style={styles.lastMsgText}>{chat.lastMessage}</span>
                  </>
                ) : (
                  <span style={styles.lastMsgText}>Нет сообщений</span>
                )}
              </span>
            </div>
          </div>
        ))}
      </div>
      <div style={styles.footer}>
        <button style={styles.footerBtn} title="Настройки">
          <span role="img" aria-label="settings">&#9881;</span>
        </button>
        <button style={styles.footerBtn} title="Профиль">
          <span role="img" aria-label="user">&#128100;</span>
        </button>
        <button style={styles.footerBtn} title="Новый чат">
          <span role="img" aria-label="new chat">&#128172;</span>
        </button>
      </div>
    </div>
  );
}

const styles = {
  list: {
    width: "300px",
    background: "#fff",
    display: "flex",
    flexDirection: "column",
    borderRight: "1px solid #dde9f0",
    height: "100%",
    minWidth: "260px",
    maxWidth: "340px",
  },
  searchBox: {
    display: "flex",
    alignItems: "center",
    padding: "10px 12px",
    borderBottom: "1px solid #dde9f0",
    background: "#f6fafd",
    position: "relative",
  },
  search: {
    flex: 1,
    padding: "8px 32px 8px 10px",
    border: "1px solid #dde9f0",
    borderRadius: "8px",
    fontSize: "15px",
    background: "#f6fafd",
    outline: "none",
  },
  searchIcon: {
    position: "absolute",
    right: 20,
    color: "#aaa",
    fontSize: "18px",
    pointerEvents: "none",
  },
  chats: {
    flex: 1,
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "0px",
    background: "#fff",
    minHeight: 0,
  },
  item: {
    display: "flex",
    alignItems: "center",
    padding: "14px 16px",
    cursor: "pointer",
    borderBottom: "1px solid #f1f1f1",
    gap: "14px",
    transition: "background 0.18s",
    minHeight: "56px",
  },
  circle: {
    width: "38px",
    height: "38px",
    borderRadius: "50%",
    display: "inline-block",
    marginRight: "2px",
    border: "2px solid #dde9f0",
  },
  chatInfo: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    minWidth: 0,
  },
  titleRow: {
    display: "flex",
    alignItems: "center",
    gap: "6px",
  },
  title: {
    fontWeight: "bold",
    color: "#222",
    fontSize: "17px",
    marginBottom: "2px",
    whiteSpace: "nowrap",
    overflow: "hidden",
    textOverflow: "ellipsis",
    maxWidth: "150px",
  },
  lastMsg: {
    color: "#888",
    fontSize: "14px",
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
    maxWidth: "170px",
  },
  lastMsgPrefix: {
    color: "#888",
    fontWeight: "600",
  },
  lastMsgText: {},
  empty: {
    color: "#aaa",
    textAlign: "center",
    marginTop: "30px",
  },
  footer: {
    padding: "8px 0",
    background: "#f6fafd",
    borderTop: "1px solid #dde9f0",
    display: "flex",
    justifyContent: "space-around",
    alignItems: "center",
  },
  footerBtn: {
    background: "none",
    border: "none",
    fontSize: "26px",
    color: "#7d8fa6",
    cursor: "pointer",
    outline: "none",
    padding: "4px 10px",
    borderRadius: "6px",
    transition: "background 0.18s",
  },
};