import React, { useState } from "react";
import AuthTabs from "../../features/auth/components/AuthTabs";
import styles from "./LoginPage.module.scss";

const LoginPage = () => (
  <div className={styles.loginPage}>
    <AuthTabs />
  </div>
);

export default LoginPage;