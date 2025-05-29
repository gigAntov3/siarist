import { Separator } from '../../../../shared/ui/separator';
import { BasketProductCard } from '../product-card';
import type { Basket } from '../../../../shared/api/basket/model';

import styles from './styles.module.css';

import { useState } from 'react';

type Props = {
  baskets: Basket[];
  onQuantityChange: (basketId: number, newQuantity: number) => void;
};

export const BasketProductList = ({ baskets: initialBaskets, onQuantityChange }: Props) => {
  const [baskets, setBaskets] = useState(initialBaskets);

  const handleDelete = (basketId: number) => {
    setBaskets(prev => prev.filter(b => b.id !== basketId));
  };

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
            photo={basket.product.photo}
            onQuantityChange={(newQty) => onQuantityChange(basket.id, newQty)}
            onDelete={() => handleDelete(basket.id)}
          />
          {index !== baskets.length - 1 && <Separator />}
        </div>
      ))}
    </div>
  );
};