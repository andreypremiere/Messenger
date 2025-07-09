import React, { useState } from "react";
import Button from "../../../shared/ui/button/Button";
import Input from "../../../shared/ui/input/Input";
import styles from "./RegisterForm.module.scss";

const RegisterForm = ({ onSuccess }) => {
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Тут отправка данных на регистрацию
    onSuccess({ phone, email, password });
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <Input
        placeholder="Номер телефона"
        value={phone}
        onChange={e => setPhone(e.target.value)}
        required
      />
      <Input
        placeholder="Электронная почта"
        type="email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <Input
        placeholder="Пароль"
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <Button type="submit">Получить код</Button>
    </form>
  );
};

export default RegisterForm;