import React, { useState } from "react";
import ChatList from "../components/Chat/ChatList";
import ChatWindow from "../components/Chat/ChatWindow";

const demoChats = [
  {
    id: 1,
    title: "никнейм",
    color: "#ffe066",
    lastMessage: "Последнее сообщение от никнейм...",
    messages: [
      { text: "Привет", isMe: false },
      { text: "Как дела? у меня все хорошо", isMe: false },
      { text: "Здорово!", isMe: true },
    ],
  },
  {
    id: 2,
    title: "1111",
    color: "#7cefff",
    lastMessage: "Последнее сообщение от 1111...",
    messages: [],
  },
  {
    id: 3,
    title: "2222",
    color: "#6fa8dc",
    lastMessage: "",
    messages: [],
  },
];

export default function ChatPage() {
  const [chats, setChats] = useState(demoChats);
  const [selectedId, setSelectedId] = useState(chats[0].id);

  function handleSelectChat(id) {
    setSelectedId(id);
  }

  function handleSendMessage(text) {
    setChats(chs =>
      chs.map(chat =>
        chat.id === selectedId
          ? {
              ...chat,
              messages: [...chat.messages, { text, isMe: true }],
              lastMessage: text,
            }
          : chat
      )
    );
  }

  const selectedChat = chats.find(c => c.id === selectedId);

  return (
    <div style={styles.container}>
      <ChatList
        chats={chats}
        selectedId={selectedId}
        onSelect={handleSelectChat}
      />
      <div style={styles.chatArea}>
        <ChatWindow
            chat={selectedChat}
            messages={selectedChat?.messages || []}
            onSendMessage={handleSendMessage}
            />
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    height: "100vh",
    background: "#f6fafd",
  },
  chatArea: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    background: "#eaf6fb",
    minWidth: 0,
  },
};