import styles from "./styles.module.css";

import SuccessImage from "./assets/success.png";
import ErrorImage from "./assets/error.png";

export const PaymentStatusPage = () => {
    const status = "processing";

    return (
        <div className={styles.wrapper}>
            {status === "processing" && (
                <>
                    <div className={styles.spinner}></div>
                    <div className={styles.status}>Платёж обрабатывается</div>
                </>
            )}

            {status === "success" && (
                <>
                    <img src={SuccessImage} alt="success" />
                    <div className={styles.status}>Платёж выполнен</div>
                </>
            )}

            {status === "error" && (
                <>
                    <img src={ErrorImage} alt="error" />
                    <div className={styles.status}>Платёж отклонён</div>
                </>
            )}
        </div>
    );

};
