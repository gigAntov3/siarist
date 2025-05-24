import ProductImage from './assets/product.png';

import HomeIcon from './assets/home.svg?react';
import BusketIcon from './assets/busket.svg?react';
import StarIcon from './assets/star.svg?react';
import FeedbackIcon from './assets/feedback.svg?react';

import styles from './styles.module.css'
import { Link } from 'react-router-dom';


export const ProductPage = () => {
    return (
        <div>
            <div className={styles.wrapper}>
                <img className={styles.productPhoto} src={ ProductImage } alt="product" />

                <div className={styles.productName}>EA SPORTS FC™ 24  —  16 000 FC Points</div>

                <div className={styles.productDescription}>FC Points — это переименованные очки FIFA, которые теперь используются в играх EA FC. Их можно потратить на покупку наборов карт, участие в драфтах EA FC Ultimate Team и покупки в магазине.</div>

                <div className={styles.productPrice}>16 000 ₽</div>

                <div className={styles.productBuy}>
                    <p>Купить</p>
                </div>
            </div>
            <div className={styles.tabBar}>
                <Link to={'/'}>
                    <HomeIcon />
                </Link>
                <Link to={'/bonus'}>
                    <StarIcon />
                </Link>
                <Link to={'/feedback'}>
                    <FeedbackIcon />
                </Link>
                <Link to={'/busket'}>
                    <BusketIcon />
                </Link>
            </div>
        </div>
    )
};