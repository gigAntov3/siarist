import { useState } from "react";
import { createPortal } from "react-dom";
import { useNavigate } from "react-router-dom";

import { ReactComponent as CheckIcon } from "./assets/check.svg";
import { ReactComponent as ChevronLeftIcon } from "./assets/chevron-left.svg";

import styles from "./styles.module.css";

export const EnterDataPage = ({ onClose }: { onClose: () => void }) => {
  const [platform, setPlatform] = useState("Google Play");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPlatform(event.target.value);
  };

  const handleSubmit = () => {
    onClose(); // Закрываем текущую модалку, BusketPage покажет следующую
  };

  return createPortal(
    <div className={styles.modalOverlay} onClick={onClose}>
      <div
        className={styles.modalContent}
        onClick={(e) => e.stopPropagation()}
      >
        <div className={styles.header}>
          <ChevronLeftIcon
            className={styles.backIcon}
            onClick={onClose}
          />
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

        <button className={styles.button} onClick={handleSubmit}>
          Сохранить
        </button>
      </div>
    </div>,
    document.body
  );
};
