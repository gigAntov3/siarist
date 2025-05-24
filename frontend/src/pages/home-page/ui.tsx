import FifaImage from './assets/fifa.png';
import ProductImage from './assets/product.png';
import UserImage from './assets/user.png';

import styles from './styles.module.css';
import { Link } from 'react-router-dom';
import { TabBar } from '../../shared/ui/tabbar';

export const HomePage = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.imageContainer}>
                <img src={FifaImage} alt="fifa" />
            </div>

            <div className={styles.dotsContainer}>
                <span className={`${styles.dot} ${styles.active}`}></span>
                <span className={styles.dot}></span>
                <span className={styles.dot}></span>
            </div>

            <div className={styles.productsContainer}>
                <span className={styles.categoryName}>Игровая валюта</span>

                <div className={styles.productsList}>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                </div>

                <hr className={styles.separator} />

                <span className={styles.categoryName}>Звездный абонемент</span>

                <div className={styles.productsList}>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                    <div className={styles.productItem}>
                        <img src={ProductImage} alt="product" />
                        <span className={styles.productName}>EA SPORTS FC™ 24 — 12 000 FC Points</span>
                        <span className={styles.productPrice}>12 000 ₽</span>
                        <Link className={styles.productInfo} to="/product">
                            Купить
                        </Link>
                    </div>
                </div>
            </div>

            <div className={styles.feedbackContainer}>
                <span className={styles.feedbackTitle}>Отзывы</span>


                <div className={styles.feedback}>
                    <div className={styles.feedbackDate}>16 мая 2024</div>
                    <div className={styles.feedbackText}>Сделали быстро и прозрачно. Простое и понятное оформление заказа</div>

                    <div className={styles.feedbackUser}>
                        <img className={styles.feedbackUserPhoto} src={UserImage} alt="user" />
                        <div className={styles.feedbackUserName}>Dani*******</div>
                    </div>

                </div>

                <hr className={styles.separator} />

                <div className={styles.feedback}>
                    <div className={styles.feedbackDate}>16 мая 2024</div>
                    <div className={styles.feedbackText}>Сделали быстро и прозрачно. Простое и понятное оформление заказа</div>

                    <div className={styles.feedbackUser}>
                        <img className={styles.feedbackUserPhoto} src={UserImage} alt="user" />
                        <div className={styles.feedbackUserName}>Dani*******</div>
                    </div>

                </div>

                <hr className={styles.separator} />

                <div className={styles.feedback}>
                    <div className={styles.feedbackDate}>16 мая 2024</div>
                    <div className={styles.feedbackText}>Сделали быстро и прозрачно. Простое и понятное оформление заказа</div>

                    <div className={styles.feedbackUser}>
                        <img className={styles.feedbackUserPhoto} src={UserImage} alt="user" />
                        <div className={styles.feedbackUserName}>Dani*******</div>
                    </div>

                </div>
            </div>

            <TabBar />
        </div>
    );
};
