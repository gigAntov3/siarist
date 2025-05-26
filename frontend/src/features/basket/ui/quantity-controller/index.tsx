import { useState } from "react";
import PlusIcon from '../../assets/plus.svg?react';
import MinusIcon from '../../assets/minus.svg?react';

import styles from "./styles.module.css";

import { decreaseBasketQuantity, increaseBasketQuantity } from "../../../../shared/api/basket";

type Props = {
  basketId: number;
  quantity: number;
  onQuantityChange?: (newQuantity: number) => void;
};

export const QuantityController = ({ basketId, quantity, onQuantityChange }: Props) => {
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
    if (loading || currentQuantity <= 1) return;

    setLoading(true);
    const ok = await decreaseBasketQuantity(basketId);
    if (ok) {
      const newQuantity = currentQuantity - 1;
      setCurrentQuantity(newQuantity);
      onQuantityChange?.(newQuantity);
    }
    setLoading(false);
  };

  return (
    <div className={styles.productControls}>
      <button className={styles.controlButton} onClick={handleIncrease} disabled={loading}>
        <PlusIcon />
      </button>
      <span className={styles.quantity}>{currentQuantity}</span>
      <button className={styles.controlButton} onClick={handleDecrease} disabled={loading || currentQuantity <= 1}>
        <MinusIcon />
      </button>
    </div>
  );
};