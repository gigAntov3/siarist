import { Link } from "react-router-dom";
import styles from './product-card.module.css';

type Props = {
    id: number;
    name: string;
    price: number;
    image: string;
};

export const ProductCard = ({ id, name, price, image }: Props) => {
    return (
        <div className={styles.card}>
            <img src={image} alt="product" />
            <span className={styles.name}>{name}</span>
            <span className={styles.price}>{price.toLocaleString("ru-RU")} ₽</span>
            <Link className={styles.buyButton} to={`/product/${id}`}>
                Купить
            </Link>
        </div>
    );
};
