import React, { useState } from "react";
import Button from "../../../shared/ui/button/Button"
import Input from "../../../shared/ui/input/Input";
import styles from "./LoginForm.module.scss";

const LoginForm = ({ onSuccess }) => {
  const [value, setValue] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь можешь вызвать API для отправки кода
    onSuccess({ value });
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <Input
        placeholder="Телефон, эл. почта или никнейм"
        value={value}
        onChange={e => setValue(e.target.value)}
        required
      />
      <Button type="submit">Получить код</Button>
    </form>
  );
};

export default LoginForm;