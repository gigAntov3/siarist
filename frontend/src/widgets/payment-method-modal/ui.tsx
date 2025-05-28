import { useState } from "react";
import { createPortal } from "react-dom";

import BankCardIcon from "./assets/bank-card.svg?react";
import SbpIcon from "./assets/sbp.svg?react";

import CheckIcon from "./assets/check.svg?react";
import ChevronLeftIcon from "./assets/chevron-left.svg?react";

import styles from "./styles.module.css";

export const PaymentMethodModal = ({ onClose }: { onClose: () => void }) => {
  const [method, setMethod] = useState("Банковская карта");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMethod(event.target.value);
  };

  const handleSubmit = () => {
    onClose();
    // Здесь можно вызвать логику оплаты или редирект
  };

  const methods = [
    {
      name: "Банковская карта",
      icon: <BankCardIcon className={styles.methodIcon} />,
    },
    {
      name: "СБП / QR-код",
      icon: <SbpIcon className={styles.methodIcon} />,
    },
  ];

  return createPortal(
    <div className={styles.modalOverlay} onClick={onClose}>
      <div
        className={styles.modalContent}
        onClick={(e) => e.stopPropagation()}
      >
        <div className={styles.header}>
          <ChevronLeftIcon className={styles.backIcon} onClick={onClose} />
          <h2 className={styles.title}>Способы оплаты</h2>
        </div>

        <div className={styles.radioGroup}>
          {methods.map(({ name, icon }) => (
            <label key={name} className={styles.radioItem}>
              <span className={styles.radioName}>
                {icon}
                {name}
              </span>
              <div
                className={`${styles.radioCustom} ${
                  method === name ? styles.radioSelected : ""
                }`}
                onClick={() => setMethod(name)}
              >
                {method === name ? (
                  <CheckIcon className={styles.chevronIcon} />
                ) : (
                  <input
                    type="radio"
                    name="paymentMethod"
                    value={name}
                    checked={method === name}
                    onChange={handleChange}
                    className={styles.radioInput}
                  />
                )}
              </div>
            </label>
          ))}
        </div>

        <button className={styles.button} onClick={handleSubmit}>
          Оплатить
        </button>
      </div>
    </div>,
    document.body
  );
};
