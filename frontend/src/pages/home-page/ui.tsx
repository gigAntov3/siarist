import { useEffect, useState } from "react";
import styles from './styles.module.css';
import { TabBar } from '../../shared/ui/tabbar';
import { PromoCarousel } from '../../widgets/promo-carousel';
import { Separator } from '../../shared/ui/separator';
import { FeedbackCard } from '../../features/feedback/ui/feedback-card';
import { Catalog } from '../../widgets/catalog/ui';
import type { Feedback } from "../../shared/api/feedback/model";
import { getFeedbacks, getFeedbacksCount } from "../../shared/api/feedback"; // ⬅️ добавили getFeedbacksCount
import { Link } from "react-router-dom";

export const HomePage = () => {
    const [feedbacks, setFeedbacks] = useState<Feedback[]>([]);
    const [feedbackCount, setFeedbackCount] = useState<number>(0); // ⬅️ новое состояние

    const offset = 0;
    const limit = 3;

    useEffect(() => {
        loadFeedbacks();
        loadFeedbackCount(); // ⬅️ загрузка количества отзывов
    }, []);

    const loadFeedbacks = async () => {
        const newFeedbacks = await getFeedbacks(limit, offset);
        setFeedbacks(newFeedbacks);
    };

    const loadFeedbackCount = async () => {
        const count = await getFeedbacksCount();
        setFeedbackCount(count);
    };

    return (
        <div className={styles.wrapper}>
            <PromoCarousel />
            <Catalog />

            <div className={styles.feedbackContainer}>
                <div className={styles.titleWrapper}>
                    <span className={styles.feedbackTitle}>Отзывы</span>
                    <span className={styles.numberReviews}>{feedbackCount}</span>
                </div>

                {feedbacks.map((feedback, index) => (
                    <div className={styles.feedback} key={feedback.id}>
                        <FeedbackCard
                            date={new Date(feedback.created_at).toLocaleDateString('ru-RU', {
                                day: 'numeric',
                                month: 'long',
                                year: 'numeric'
                            })}
                            text={feedback.content}
                            userName={feedback.author.username}
                        />
                        {index < feedbacks.length - 1 && <Separator />}
                    </div>
                ))}

                <Link to="/feedback">
                    <div className={styles.feedbackButton}>Посмотреть все</div>
                </Link>
            </div>

            <TabBar />
        </div>
    );
};