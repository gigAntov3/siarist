import { useState } from "react";
import PlusIcon from '../../assets/plus.svg?react';
import MinusIcon from '../../assets/minus.svg?react';

import styles from "./styles.module.css";

import { decreaseBasketQuantity, deleteBasket, increaseBasketQuantity } from "../../../../shared/api/basket";

type Props = {
  basketId: number;
  quantity: number;
  onQuantityChange?: (newQuantity: number) => void;
  onDelete?: () => void; // ✅ добавляем проп
};

export const QuantityController = ({ basketId, quantity, onQuantityChange, onDelete }: Props) => {
  const [currentQuantity, setCurrentQuantity] = useState<number>(quantity);
  const [loading, setLoading] = useState(false);

  const handleIncrease = async () => {
    if (loading) return;

    setLoading(true);
    const ok = await increaseBasketQuantity(basketId);
    if (ok) {
      const newQuantity = currentQuantity + 1;
      setCurrentQuantity(newQuantity);
      onQuantityChange?.(newQuantity);
    }
    setLoading(false);
  };

  const handleDecrease = async () => {
    if (loading) return;
    setLoading(true);

    let ok = false;

    if (currentQuantity <= 1) {
      ok = await deleteBasket(basketId);
      if (ok) {
        onQuantityChange?.(0); // можно использовать, если родителю нужно знать
        onDelete?.(); // ✅ вызываем onDelete
      }
    } else {
      ok = await decreaseBasketQuantity(basketId);
      if (ok) {
        const newQuantity = currentQuantity - 1;
        setCurrentQuantity(newQuantity);
        onQuantityChange?.(newQuantity);
      }
    }

    setLoading(false);
  };

  return (
    <div className={styles.productControls}>
      <button className={styles.controlButton} onClick={handleIncrease} disabled={loading}>
        <PlusIcon />
      </button>
      <span className={styles.quantity}>{currentQuantity}</span>
      {/* ✅ теперь кнопка не дизейблится при quantity === 1 */}
      <button className={styles.controlButton} onClick={handleDecrease} disabled={loading}>
        <MinusIcon />
      </button>
    </div>
  );
};