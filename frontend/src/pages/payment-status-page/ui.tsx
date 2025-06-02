import { Link, useSearchParams } from "react-router-dom";
import styles from "./styles.module.css";

import SuccessImage from "./assets/success.png";
import ErrorImage from "./assets/error.png";

export const PaymentStatusPage = () => {
    const [searchParams] = useSearchParams();
    const status = searchParams.get("status");

    const isValidStatus = ["processing", "success", "error"].includes(status || "");

    return (
        <div className={styles.page}>
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

                {!isValidStatus && (
                    <div className={styles.status}>Некорректный статус платежа</div>
                )}
            </div>

            {(status === "success" || status === "error") && (
                <Link to="/" className={styles.mainButton}>На главную</Link>
            )}
        </div>
    );
};



