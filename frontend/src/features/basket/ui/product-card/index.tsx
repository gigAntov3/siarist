import { QuantityController } from '../quantity-controller';

import ProductImage from '../../assets/product.png';

import styles from "./styles.module.css";

type Props = {
    basketId: number
    name: string;
    price: number;
    quantity: number;
    photo: string
    onQuantityChange?: (newQuantity: number) => void;
}

export const BasketProductCard = ({ basketId, name, price, quantity, photo, onQuantityChange }: Props) => {
  return (
    <div className={styles.productItem}>
      <img className={styles.productImage} src={photo || ProductImage} alt="product" />

      <div className={styles.productInfo}>
        <div className={styles.productName}>{name}</div>
        <div className={styles.productPrice}>{price.toLocaleString()} ₽</div>
      </div>

      <QuantityController
        basketId={basketId}
        quantity={quantity}
        onQuantityChange={onQuantityChange}
      />
    </div>
  );
};
