import { createPortal } from "react-dom";

import { ReactComponent as CheckIcon } from "./assets/check.svg";
import { ReactComponent as ChevronLeftIcon } from "./assets/chevron-left.svg";

import styles from "./styles.module.css";

type Props = {
  onClose: () => void;
  onSave: () => void;
  platform: string;
  setPlatform: (value: string) => void;
  email: string;
  setEmail: (value: string) => void;
  password: string;
  setPassword: (value: string) => void;
  username: string;
  setUsername: (value: string) => void;
};

export const EnterAccountModal = ({
  onClose,
  onSave,
  platform,
  setPlatform,
  email,
  setEmail,
  password,
  setPassword,
  username,
  setUsername,
}: Props) => {
  const platforms = [
    { code: "ea", name: "EA" },
    { code: "google", name: "Google Play" },
    { code: "facebook", name: "Facebook" },
  ];

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPlatform(event.target.value);
  };

  const handleSubmit = () => {
    onSave();
  };

  return createPortal(
    <div className={styles.modalOverlay} onClick={onClose}>
      <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
        <div className={styles.header}>
          <ChevronLeftIcon className={styles.backIcon} onClick={onClose} />
          <h2 className={styles.title}>Подтвердите данные</h2>
        </div>

        <div className={styles.radioGroup}>
          {platforms.map(({ code, name }) => (
            <label key={code} className={styles.radioItem}>
              <span className={styles.radioName}>{name}</span>
              <div
                className={`${styles.radioCustom} ${
                  platform === code ? styles.radioSelected : ""
                }`}
                onClick={() => setPlatform(code)}
              >
                {platform === code ? (
                  <CheckIcon className={styles.chevronIcon} />
                ) : (
                  <input
                    type="radio"
                    name="platform"
                    value={code}
                    checked={platform === code}
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
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        {platform !== "ea" && (
          <input
            className={styles.input}
            type="password"
            placeholder="●●●●●●●"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        )}

        <input
          className={styles.input}
          type="text"
          placeholder="Имя аккаунта"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <button className={styles.button} onClick={handleSubmit}>
          Сохранить
        </button>
      </div>
    </div>,
    document.body
  );
};
