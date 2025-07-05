import React, { useRef } from "react";

export default function CodeInput({ length = 6, onComplete }) {
  const inputs = Array.from({ length });
  const refs = React.useRef([...Array(length)].map(() => React.createRef()));

  function handleChange(e, i) {
    const value = e.target.value.replace(/\D/, "");
    e.target.value = value;

    if (value && i < refs.length - 1) {
      refs[i + 1].current.focus();
    }
    if (refs.every(ref => ref.current.value !== "")) {
      onComplete(refs.map(ref => ref.current.value).join(""));
    }
  }

  function handleKeyDown(e, i) {
    if (e.key === "Backspace" && !e.target.value && i > 0) {
      refs[i - 1].current.focus();
    }
  }

  return (
    <div style={styles.container}>
      <div style={styles.box}>
        <div style={styles.label}>Введите полученный код</div>
        <div style={styles.inputs}>
          {inputs.map((_, i) => (
            <input
              key={i}
              ref={refs[i]}
              maxLength={1}
              style={styles.input}
              onChange={e => handleChange(e, i)}
              onKeyDown={e => handleKeyDown(e, i)}
              inputMode="numeric"
              pattern="[0-9]*"
              autoFocus={i === 0}
            />
          ))}
        </div>
      </div>
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
  box: {
    padding: "32px",
    borderRadius: "8px",
    background: "#fff",
    boxShadow: "0 2px 10px #0001",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    minWidth: "320px",
  },
  label: {
    marginBottom: "16px",
    fontSize: "18px",
    fontWeight: "bold",
    color: "#222",
  },
  inputs: {
    display: "flex",
    gap: "8px",
  },
  input: {
    width: "40px",
    height: "48px",
    fontSize: "28px",
    textAlign: "center",
    border: "1px solid #c2e3fa",
    borderRadius: "6px",
    outline: "none",
  },
};