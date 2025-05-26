import styles from './styles.module.css';
import { TabBar } from '../../shared/ui/tabbar';
import { PromoCarousel } from '../../widgets/promo-carousel';
// import { ProductList } from '../../features/products/ui/product-list';
import { Separator } from '../../shared/ui/separator';
import { FeedbackCard } from '../../features/feedback/ui/feedback-card';
import { Catalog } from '../../widgets/catalog/ui';

export const HomePage = () => {
    return (
        <div className={styles.wrapper}>
            <PromoCarousel />

            <Catalog />

            {/* <div className={styles.productsContainer}>
                <ProductList title="Игровая валюта" category_id={1} />

                <Separator />

                <ProductList title="Звездный абонемент" category_id={2} />
            </div> */}

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
