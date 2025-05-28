import { useEffect, useState } from 'react';

import CardImage from './assets/card.png';
import styles from './styles.module.css';

import BlackCircleIcon from './assets/black-circle.svg?react';
import GreenBlankCircleIcon from './assets/green-blank-circle.svg?react';
import GreenCircleIcon from './assets/green-circle.svg?react';
import ExplosionIcon from './assets/explosion.svg?react';

import { TabBar } from '../../shared/ui/tabbar';
import { getUser } from '../../shared/api/users';
import { BonusCard } from '../../shared/ui/bonus-card';

export const BonusPage = () => {
    const [completedPurchases, setCompletedPurchases] = useState<number>(0);
    const [balance, setBalance] = useState<number>(0);

    const milestones = [
        { step: 1, label: '1 покупка — 50 ₽ на баланс' },
        { step: 3, label: '3 покупка — 75 ₽ на баланс' },
        { step: 5, label: '5 покупка — Усилитель B' },
        { step: 10, label: '10 покупка — 50 ₽ на баланс' },
        { step: 15, label: '15 покупка — 75 ₽ на баланс' },
        { step: 20, label: '20 покупка — Секретный подарок' },
        { step: 30, label: '30 покупка — 200 ₽ на баланс' },
        { step: 40, label: '40 покупка — 250 ₽ на баланс' },
        { step: 50, label: '50 покупка — Любой абонемент' },
        { step: 60, label: '60 покупка — 350 ₽ на баланс' },
        { step: 70, label: '70 покупка — 400 ₽ на баланс' },
        { step: 80, label: '80 покупка — 450 ₽ на баланс' },
        { step: 90, label: '90 покупка — 500 ₽ на баланс' },
        { step: 100, label: '100 покупка — 20 000 FC Points', isLast: true },
    ];

    const isMaxedOut = completedPurchases >= 100;

    const nextMilestone = milestones.find(m => m.step > completedPurchases);
    const remainingToNext = nextMilestone ? nextMilestone.step - completedPurchases : 0;

    const prevMilestone = [...milestones]
        .reverse()
        .find((m) => m.step <= completedPurchases) ?? { step: 0 };

    const progressRange = nextMilestone ? nextMilestone.step - prevMilestone.step : 1;
    const progressWithinRange = completedPurchases - prevMilestone.step;
    const progressPercent = isMaxedOut
        ? 100
        : Math.min((progressWithinRange / progressRange) * 100, 100);

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const userId = 1; // заменить на актуальное получение user_id
                const user = await getUser(userId);
                setCompletedPurchases(user.purchases_count);
                setBalance(user.balance);
            } catch (error) {
                console.error('Ошибка при получении пользователя:', error);
            }
        };

        fetchUserData();
    }, []);

    return (
        <div className={styles.wrapper}>
            <div className={styles.imageContainer}>

                <BonusCard />

                <div className={styles.overlay}>
                    <h2 className={styles.bonusTitle}>Бонусы</h2>
                    <p className={styles.bonusText}>Покупайте и получайте бонусы рублями</p>
                    <div className={styles.amount}>{balance} ₽</div>
                    <div className={styles.progressBar}>
                        <div
                            className={styles.progressFill}
                            style={{ width: `${progressPercent}%` }}
                        ></div>
                    </div>
                    <p className={styles.progressText}>
                        {isMaxedOut
                            ? '🎉 Все награды получены!'
                            : `${completedPurchases} покуп${completedPurchases === 1 ? 'ка' : 'ки'}, ещё ${remainingToNext} до следующего бонуса`}
                    </p>
                </div>
            </div>

            <div className={styles.reviewReward}>
                Получите <strong>25 ₽</strong> за первый отзыв после 2-й покупки
            </div>
            <button className={styles.button}>К товарам</button>

            <hr className={styles.separator} />

            <div className={styles.map}>
                <h3 className={styles.mapTitle}>Карта</h3>
                <ul className={styles.milestones}>
                    {milestones.map(({ step, label, isLast }, index) => {
                        const isActive = completedPurchases >= step;
                        const isNext = completedPurchases < step &&
                            milestones.find(m => m.step > completedPurchases)?.step === step;

                        let IconComponent;
                        if (isLast) {
                            IconComponent = ExplosionIcon;
                        } else if (isActive) {
                            IconComponent = GreenCircleIcon;
                        } else if (isNext) {
                            IconComponent = GreenBlankCircleIcon;
                        } else {
                            IconComponent = BlackCircleIcon;
                        }

                        return (
                            <li key={index} className={styles.milestoneItem}>
                                <IconComponent
                                    className={`${styles.milestoneIcon} ${isLast ? styles.lastIcon : ''}`}
                                />
                                <span className={isActive ? styles.activeText : styles.inactiveText}>
                                    {label}
                                </span>
                            </li>
                        );
                    })}
                </ul>
            </div>

            <TabBar />
        </div>
    );
};
