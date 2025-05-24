import { FeedbackCard } from '../../features/feedback/ui/feedback-card';
import { Separator } from '../../shared/ui/separator';
import { TabBar } from '../../shared/ui/tabbar';
import styles from './styles.module.css';


const feedbacks = [
    {
        date: '16 мая 2024',
        text: 'Все понравилось! Заказ оформили за пару минут, всё прозрачно и честно.',
        userName: 'Elena******',
    },
    {
        date: '17 мая 2024',
        text: 'Хороший сервис. Немного пришлось подождать, но результат устроил.',
        userName: 'Ivan*******',
    },
    {
        date: '18 мая 2024',
        text: 'Очень быстро и удобно. Рекомендую всем, кто ценит своё время.',
        userName: 'Nata*******',
    },
    {
        date: '19 мая 2024',
        text: 'Не совсем понял процесс оформления, но оператор быстро помог. Спасибо!',
        userName: 'Sergei*****',
    },
    {
        date: '20 мая 2024',
        text: 'Все прошло гладко. Никаких скрытых условий, что приятно удивило.',
        userName: 'Olga*******',
    },
    {
        date: '21 мая 2024',
        text: 'Могло быть и быстрее. Но в целом всё понятно и по делу.',
        userName: 'Alexey****',
    },
    {
        date: '22 мая 2024',
        text: 'Прекрасный опыт! Сайт интуитивно понятный, оформление заняло пару минут.',
        userName: 'Tatiana***',
    },
    {
        date: '23 мая 2024',
        text: 'Не понравилось, что пришлось загружать документы дважды. Поддержка сработала хорошо.',
        userName: 'Roman*****',
    },
    {
        date: '24 мая 2024',
        text: 'Сервис на высоте! Уже третий раз пользуюсь — всё стабильно и без проблем.',
        userName: 'Marina****',
    },
    {
        date: '25 мая 2024',
        text: 'Было немного непонятно на этапе выбора услуги, но в остальном отлично.',
        userName: 'Dmitriy***',
    },
    {
        date: '26 мая 2024',
        text: 'Не сделали быстро и прозрачно. Была путаница в деталях заказа.',
        userName: 'Andrei****',
    },
];


export const FeedbackPage = () => {
    return (
        <div>
            <div className={styles.feedbackContainer}>
                <div className={styles.titleWrapper}>
                    <span className={styles.feedbackTitle}>Отзывы</span>
                    <span className={styles.numberReviews}>5000</span>
                </div>

                {feedbacks.map((fb, idx) => (
                    <div className={styles.feedbackItems} key={idx}>
                        <FeedbackCard {...fb} />
                        {idx !== feedbacks.length - 1 && <Separator />}
                    </div>
                ))}
            </div>

            <TabBar />
        </div>
    );
};