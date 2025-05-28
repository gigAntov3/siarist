import styles from './styles.module.css';
import { TabBar } from '../../shared/ui/tabbar';
import { PromoCarousel } from '../../widgets/promo-carousel';
import { Separator } from '../../shared/ui/separator';
import { FeedbackCard } from '../../features/feedback/ui/feedback-card';
import { Catalog } from '../../widgets/catalog/ui';

export const HomePage = () => {
    return (
        <div className={styles.wrapper}>
            <PromoCarousel />

            <Catalog />

            <div className={styles.feedbackContainer}>
                <span className={styles.feedbackTitle}>Отзывы</span>

                <FeedbackCard date="16 мая 2024" text="Сделали быстро и прозрачно. Простое и понятное оформление заказа" userName="Dani******" />

                <Separator />

                <FeedbackCard date="16 мая 2024" text="Сделали быстро и прозрачно. Простое и понятное оформление заказа" userName="Dani******" />

                <Separator />

                <FeedbackCard date="16 мая 2024" text="Сделали быстро и прозрачно. Простое и понятное оформление заказа" userName="Dani******" />
            </div>

            <TabBar />
        </div>
    );
};
