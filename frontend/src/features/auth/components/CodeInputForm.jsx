import React, { useState, useRef } from "react";
import Button from "../../../shared/ui/button/Button";
import styles from "./CodeInputForm.module.scss";

const CodeInputForm = ({ onBack }) => {
  const [code, setCode] = useState(["", "", "", "", "", ""]);
  const inputsRef = useRef([]);

  const handleChange = (index, val) => {
    if (/^\d?$/.test(val)) {
      const next = [...code];
      next[index] = val;
      setCode(next);

      // Переход к следующему инпуту, если введено число и не последний инпут
      if (val && index < code.length - 1) {
        inputsRef.current[index + 1]?.focus();
      }
    }
  };

  // Позволяет удалять цифру и переходить назад по Backspace
  const handleKeyDown = (index, e) => {
    if (e.key === "Backspace" && !code[index] && index > 0) {
      inputsRef.current[index - 1]?.focus();
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Проверка кода (API)
    // ...
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <div className={styles.label}>Введите полученный код</div>
      <div className={styles.codeRow}>
        {code.map((c, i) => (
          <input
            key={i}
            ref={el => inputsRef.current[i] = el}
            className={styles.codeInput}
            type="text"
            maxLength={1}
            value={c}
            onChange={e => handleChange(i, e.target.value)}
            onKeyDown={e => handleKeyDown(i, e)}
            autoFocus={i === 0}
          />
        ))}
      </div>
      <Button type="button" onClick={onBack}>Назад</Button>
    </form>
  );
};

export default CodeInputForm;