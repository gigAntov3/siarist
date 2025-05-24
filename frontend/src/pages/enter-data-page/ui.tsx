import { useState } from "react";

import CheckIcon from './assets/check.svg?react';
import ChevronLeftIcon from './assets/chevron-left.svg?react';

import styles from "./styles.module.css";
import { Link } from "react-router-dom";

export const EnterDataPage = () => {
  const [platform, setPlatform] = useState("Google Play");

  const handleChange = (event) => {
    setPlatform(event.target.value);
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <Link to={'/busket'}>
            <ChevronLeftIcon className={styles.backIcon} />
        </Link>
        <h2 className={styles.title}>Подтвердите данные</h2>
      </div>

      <div className={styles.radioGroup}>
        {["EA", "Google Play", "Facebook"].map((item) => (
          <label key={item} className={styles.radioItem}>
            <span className={styles.radioName}>{item}</span>
            <div
              className={`${styles.radioCustom} ${
                platform === item ? styles.radioSelected : ""
              }`}
              onClick={() => setPlatform(item)}
            >
              {platform === item ? (
                <CheckIcon className={styles.chevronIcon} />
              ) : (
                <input
                  type="radio"
                  name="platform"
                  value={item}
                  checked={platform === item}
                  onChange={handleChange}
                  className={styles.radioInput}
                />
              )}
            </div>
          </label>
        ))}
      </div>

      <hr className={styles.separator} />

      <h2 className={styles.title}>Введите данные</h2>

      <input
        className={styles.input}
        type="email"
        placeholder="mail@romaganiev.com"
      />

      {platform !== "EA" && (
        <input
          className={styles.input}
          type="password"
          placeholder="●●●●●●●"
        />
      )}

      <input
        className={styles.input}
        type="text"
        placeholder="Имя аккаунта"
        defaultValue="romaganiev"
      />
      <Link to={'/payment-status'}>
        <button className={styles.button}>Сохранить</button>
      </Link>
    </div>
  );
};
