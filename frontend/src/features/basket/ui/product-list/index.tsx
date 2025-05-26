import { Separator } from '../../../../shared/ui/separator';
import { BasketProductCard } from '../product-card';
import type { Basket } from '../../../../shared/api/basket/model';

import styles from './styles.module.css';

type Props = {
  baskets: Basket[];
  onQuantityChange: (basketId: number, newQuantity: number) => void;
};

export const BasketProductList = ({ baskets, onQuantityChange }: Props) => {
  if (baskets.length === 0) return <div>Корзина пуста</div>;

  return (
    <div className={styles.wrapper}>
      {baskets.map((basket, index) => (
        <div className={styles.product} key={basket.id}>
          <BasketProductCard
            basketId={basket.id}
            name={basket.product.name}
            price={basket.product.price}
            quantity={basket.quantity}
            onQuantityChange={(newQty) => onQuantityChange(basket.id, newQty)}
          />
          {index !== baskets.length - 1 && <Separator />}
        </div>
      ))}
    </div>
  );
};