import styles from './feedback-card.module.css';
import UserImage from '../../../shared/assets/user.png';

interface Props {
    date: string;
    text: string;
    userName: string;
}

const maskUserName = (name: string) => {
    const length = name.length;
    if (length === 0) return '';

    const visibleLength = Math.ceil(length * 0.6);
    const maskedLength = length - visibleLength;

    const visiblePart = name.slice(0, visibleLength);
    const maskedPart = '*'.repeat(maskedLength);

    return visiblePart + maskedPart;
};

export const FeedbackCard = ({ date, text, userName }: Props) => (
    <div className={styles.feedback}>
        <div className={styles.feedbackDate}>{date}</div>
        <div className={styles.feedbackText}>{text}</div>

        <div className={styles.feedbackUser}>
            <img className={styles.feedbackUserPhoto} src={UserImage} alt="user" />
            <div className={styles.feedbackUserName}>{maskUserName(userName)}</div>
        </div>
    </div>
);