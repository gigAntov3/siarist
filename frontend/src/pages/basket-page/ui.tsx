import styles from './styles.module.css'

import PlusIcon from './assets/plus.svg?react';
import MinusIcon from './assets/minus.svg?react';

import ProductImage from './assets/product.png';
import { Link } from 'react-router-dom';
import { TabBar } from '../../shared/ui/tabbar';


export const BusketPage = () => {
    return (
        <div>
            <div className={styles.wrapper}>
                <div className={styles.title}>Корзина</div>

                <div className={styles.productItem}>
                    <img className={styles.productImage} src={ProductImage} alt="product" />

                    <div className={styles.productInfo}>
                        <div className={styles.productName}>EA SPORTS FC™ 24 — 16 000 FC Points</div>
                        <div className={styles.productPrice}>17 250 ₽</div>
                    </div>

                    <div className={styles.productControls}>
                        <button className={styles.controlButton}>
                            <PlusIcon />
                        </button>
                        <span className={styles.productQuantity}>1</span>
                        <button className={styles.controlButton}>
                            <MinusIcon />
                        </button>
                    </div>
                </div>

                

                
                <hr className={styles.separator} />

                <div className={styles.productItem}>
                    <img className={styles.productImage} src={ProductImage} alt="product" />

                    <div className={styles.productInfo}>
                        <div className={styles.productName}>EA SPORTS FC™ 24 — 16 000 FC Points</div>
                        <div className={styles.productPrice}>17 250 ₽</div>
                    </div>

                    <div className={styles.productControls}>
                        <button className={styles.controlButton}>
                            <PlusIcon />
                        </button>
                        <span className={styles.productQuantity}>1</span>
                        <button className={styles.controlButton}>
                            <MinusIcon />
                        </button>
                    </div>
                </div>

                <hr className={styles.separator} />

                <div className={styles.productItem}>
                    <img className={styles.productImage} src={ProductImage} alt="product" />

                    <div className={styles.productInfo}>
                        <div className={styles.productName}>EA SPORTS FC™ 24 — 16 000 FC Points</div>
                        <div className={styles.productPrice}>17 250 ₽</div>
                    </div>

                    <div className={styles.productControls}>
                        <button className={styles.controlButton}>
                            <PlusIcon />
                        </button>
                        <span className={styles.productQuantity}>1</span>
                        <button className={styles.controlButton}>
                            <MinusIcon />
                        </button>
                    </div>
                </div>

                <hr className={styles.separator} />

                <div className={styles.productItem}>
                    <img className={styles.productImage} src={ProductImage} alt="product" />

                    <div className={styles.productInfo}>
                        <div className={styles.productName}>EA SPORTS FC™ 24 — 16 000 FC Points</div>
                        <div className={styles.productPrice}>17 250 ₽</div>
                    </div>

                    <div className={styles.productControls}>
                        <button className={styles.controlButton}>
                            <PlusIcon />
                        </button>
                        <span className={styles.productQuantity}>1</span>
                        <button className={styles.controlButton}>
                            <MinusIcon />
                        </button>
                    </div>
                </div>


                <hr className={styles.separator} />

                <div className={styles.productItem}>
                    <img className={styles.productImage} src={ProductImage} alt="product" />

                    <div className={styles.productInfo}>
                        <div className={styles.productName}>EA SPORTS FC™ 24 — 16 000 FC Points</div>
                        <div className={styles.productPrice}>17 250 ₽</div>
                    </div>

                    <div className={styles.productControls}>
                        <button className={styles.controlButton}>
                            <PlusIcon />
                        </button>
                        <span className={styles.productQuantity}>1</span>
                        <button className={styles.controlButton}>
                            <MinusIcon />
                        </button>
                    </div>
                </div>
                


                <hr className={styles.separator} />

                <div className={styles.bonusWrapper}>
                    <div className={styles.bonusInfo}>
                        <div className={styles.bonusLabel}>Бонусы</div>
                        <div className={styles.bonusAmount}>750 ₽</div>
                    </div>
                    
                    <button className={styles.bonusButton}>Списать</button>
                </div>

                <hr className={styles.separator} />

                <div className={styles.totalWrapper}>
                    <div className={styles.totalLabel}>Итого</div>
                    <div className={styles.totalAmount}>51 750 ₽</div>
                </div>

                <Link to={'/enter-data'}>
                    <button className={styles.buyButton}>Купить</button>
                </Link>
            </div>

            <TabBar />
        </div>
    )
}