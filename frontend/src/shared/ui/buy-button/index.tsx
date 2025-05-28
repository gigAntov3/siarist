import { useState } from "react";
import styles from "./styles.module.css";

import PlusIcon from '../../assets/plus.svg?react';
import MinusIcon from '../../assets/minus.svg?react';

import {
    addProductToBasket,
    increaseBasketQuantity,
    decreaseBasketQuantity
} from "../../../shared/api/basket";

interface BuyControlProps {
    productId: number;
    userId: number;
    initialQuantity?: number;
}

export const BuyButton = ({
    productId,
    userId,
    initialQuantity = 0,
}: BuyControlProps) => {
    const [basketId, setBasketId] = useState<number | null>(null);
    const [quantity, setQuantity] = useState(initialQuantity);
    const [loading, setLoading] = useState(false);

    const handleAddToBasket = async () => {
        if (loading) return;
        setLoading(true);
        try {
            const basketId = await addProductToBasket(userId, productId, 1);
            setBasketId(basketId);
            setQuantity(1);
        } finally {
            setLoading(false);
        }
    };

    const handleIncrease = async () => {
        const success = await increaseBasketQuantity(basketId);
        if (success) setQuantity((prev) => prev + 1);
    };

    const handleDecrease = async () => {
        if (quantity <= 0) return;
        const success = await decreaseBasketQuantity(basketId);
        if (success) setQuantity((prev) => Math.max(0, prev - 1));
    };

    if (quantity > 0) {
        return (
            <div className={styles.wrapper}>
                <div className={styles.controls}>
                    <button onClick={handleDecrease} className={styles.iconButton}>
                        <MinusIcon />
                    </button>
                    <span className={styles.quantity}>{quantity}</span>
                    <button onClick={handleIncrease} className={styles.iconButton}>
                        <PlusIcon />
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div
            className={styles.wrapper}
            onClick={handleAddToBasket}
            role="button"
            aria-disabled={loading}
        >
            {loading ? "Добавление..." : "Купить"}
        </div>
    );
};