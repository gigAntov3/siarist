import React from "react";
import { Link } from "react-router-dom";


import { ReactComponent as BestPriceIcon } from '../assets/best-price.svg';
import { ReactComponent as NewIcon } from '../assets/new.svg';
import { ReactComponent as HitIcon } from '../assets/hit.svg';

import styles from './product-card.module.css';

type Tag = 'best' | 'new' | 'hit';

const tagClassNames: Record<Tag, string> = {
    best: styles.best,
    new: styles.new,
    hit: styles.hit,
};

type Props = {
    id: number;
    name: string;
    price: number;
    image: string;
    tag?: Tag;
};

const tagComponents: Record<Tag, { icon: React.ReactElement; label: string }> = {
    best: {
        icon: <BestPriceIcon />,
        label: "ЛУЧШАЯ ЦЕНА",
    },
    new: {
        icon: <NewIcon />,
        label: "НОВОЕ",
    },
    hit: {
        icon: <HitIcon />,
        label: "ХИТ ПРОДАЖ",
    },
};

export const ProductCard = ({ id, name, price, image, tag }: Props) => {
    return (
        <div className={styles.card}>
            <div className={styles.imageWrapper}>
                <img src={image} alt="product" />

                {tag && (
                    <div className={`${styles.tag} ${tagClassNames[tag]}`}>
                        <span className={tagClassNames[tag]}>
                            {React.createElement(tagComponents[tag].icon.type, { className: styles.tag })}
                            {tagComponents[tag].label}
                        </span>
                    </div>
                )}
            </div>

            <span className={styles.name}>{name}</span>
            <span className={styles.price}>{price.toLocaleString("ru-RU")} ₽</span>
            <Link className={styles.buyButton} to={`/product/${id}`}>
                Купить
            </Link>
        </div>
    );
};