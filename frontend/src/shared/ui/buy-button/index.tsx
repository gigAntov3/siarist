import { useState } from "react";
import styles from "./styles.module.css";

// import PlusIcon from '../../assets/plus.svg';
import { ReactComponent as PlusIcon } from '../../assets/plus.svg';
// import MinusIcon from '../../assets/minus.svg';
import { ReactComponent as MinusIcon } from '../../assets/minus.svg';

import {
    addProductToBasket,
    increaseBasketQuantity,
    decreaseBasketQuantity,
    deleteBasket
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
        if (!basketId) return;
        const success = await increaseBasketQuantity(basketId);
        if (success) setQuantity((prev) => prev + 1);
    };

    const handleDecrease = async () => {
        if (quantity <= 0 || !basketId) return;

        if (quantity === 1) {
            const ok = await deleteBasket(basketId);
            if (ok) {
                setQuantity(0);
                setBasketId(null);
            }
        } else {
            const success = await decreaseBasketQuantity(basketId);
            if (success) setQuantity((prev) => prev - 1);
        }
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