import styles from './feedback-card.module.css';
import UserImage from '../../../shared/assets/user.png';

interface Props {
    date: string;
    text: string;
    userName: string;
}

export const FeedbackCard = ({ date, text, userName }: Props) => (
    <div className={styles.feedback}>
        <div className={styles.feedbackDate}>{date}</div>
        <div className={styles.feedbackText}>{text}</div>

        <div className={styles.feedbackUser}>
            <img className={styles.feedbackUserPhoto} src={UserImage} alt="user" />
            <div className={styles.feedbackUserName}>{userName}</div>
        </div>
    </div>
);