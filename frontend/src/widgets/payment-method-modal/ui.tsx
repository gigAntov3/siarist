import { createPortal } from "react-dom";

// import BankCardIcon from "./assets/bank-card.svg?react";
import { ReactComponent as BankCardIcon } from "./assets/bank-card.svg";
// import SbpIcon from "./assets/sbp.svg?react";
import { ReactComponent as SbpIcon } from "./assets/sbp.svg";

// import CheckIcon from "./assets/check.svg?react";
import { ReactComponent as CheckIcon } from "./assets/check.svg";
// import ChevronLeftIcon from "./assets/chevron-left.svg?react";
import { ReactComponent as ChevronLeftIcon } from "./assets/chevron-left.svg";

import styles from "./styles.module.css";

export const PaymentMethodModal = ({
  onClose,
  selectedMethod,
  setSelectedMethod,
  onSelect,
}: {
  onClose: () => void;
  selectedMethod: string | null;
  setSelectedMethod: (method: string) => void;
  onSelect: (method: string) => void;
}) => {
  const methods = [
    {
      code: "card",
      name: "Банковская карта",
      icon: <BankCardIcon className={styles.methodIcon} />,
    },
    {
      code: "sbp",
      name: "СБП / QR-код",
      icon: <SbpIcon className={styles.methodIcon} />,
    },
  ];

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedMethod(event.target.value);
  };

  const handleSubmit = () => {
    if (selectedMethod) {
      onSelect(selectedMethod);
    }
  };

  return createPortal(
    <div className={styles.modalOverlay} onClick={onClose}>
      <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
        <div className={styles.header}>
          <ChevronLeftIcon className={styles.backIcon} onClick={onClose} />
          <h2 className={styles.title}>Способы оплаты</h2>
        </div>

        <div className={styles.radioGroup}>
          {methods.map(({ code, name, icon }) => (
            <label key={code} className={styles.radioItem}>
              <span className={styles.radioName}>
                {icon}
                {name}
              </span>
              <div
                className={`${styles.radioCustom} ${
                  selectedMethod === code ? styles.radioSelected : ""
                }`}
                onClick={() => setSelectedMethod(code)}
              >
                {selectedMethod === code ? (
                  <CheckIcon className={styles.chevronIcon} />
                ) : (
                  <input
                    type="radio"
                    name="paymentMethod"
                    value={code}
                    checked={selectedMethod === code}
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