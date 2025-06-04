import React from "react";
import { Link } from "react-router-dom";
import styles from './product-card.module.css';

// import BestPriceIcon from '../assets/best-price.svg';
import { ReactComponent as BestPriceIcon } from '../assets/best-price.svg';
// import NewIcon from '../assets/new.svg';
import { ReactComponent as NewIcon } from '../assets/new.svg';
// import HitIcon from '../assets/hit.svg';
import { ReactComponent as HitIcon } from '../assets/hit.svg';


type Props = {
    id: number;
    name: string;
    price: number;
    image: string;
    tag?: string; // e.g. ["best", "new", "hit"]
};

export const ProductCard = ({ id, name, price, image, tag }: Props) => {
    const tagComponents = {
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

    return (
        <div className={styles.card}>
            <div className={styles.imageWrapper}>
                <img src={image} alt="product" />

                {tag && tag in tagComponents && (
                    <div className={`${styles.tag} ${styles[tag]}`}>
                        {React.cloneElement(tagComponents[tag].icon, { className: styles[tag] })}
                        <span className={styles[tag]}>{tagComponents[tag].label}</span>
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