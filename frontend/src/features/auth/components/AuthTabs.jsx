import React, { useState } from "react";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import CodeInputForm from "./CodeInputForm";
import styles from "./AuthTabs.module.scss";

const AuthTabs = () => {
  const [activeTab, setActiveTab] = useState("login");
  const [step, setStep] = useState("form"); // form | code
  const [formData, setFormData] = useState({});

  const handleSuccess = (data) => {
    setFormData(data);
    setStep("code");
  };

  const handleBack = () => setStep("form");

  return (
    <div className={styles.authTabs}>
      {step === "form" && (
        <div className={styles.tabs}>
          <button
            className={activeTab === "login" ? styles.active : ""}
            onClick={() => setActiveTab("login")}
          >
            Вход
          </button>
          <button
            className={activeTab === "register" ? styles.active : ""}
            onClick={() => setActiveTab("register")}
          >
            Регистрация
          </button>
        </div>
      )}

      <div className={styles.tabContent}>
        {step === "form" ? (
          activeTab === "login" ? (
            <LoginForm onSuccess={handleSuccess} />
          ) : (
            <RegisterForm onSuccess={handleSuccess} />
          )
        ) : (
          <CodeInputForm onBack={handleBack} formData={formData} />
        )}
      </div>
    </div>
  );
};

export default AuthTabs;