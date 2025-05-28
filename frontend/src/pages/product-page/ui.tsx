import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { TabBar } from '../../shared/ui/tabbar';
import ProductImage from './assets/product.png';
import styles from './styles.module.css';

import { getProduct } from "../../shared/api/products";
import type { Product } from "../../shared/api/products/model";

import {
    addProductToBasket,
    increaseBasketQuantity,
    decreaseBasketQuantity
} from "../../shared/api/basket";

import PlusIcon from './assets/plus.svg?react';
import MinusIcon from './assets/minus.svg?react';
import { BuyButton } from "../../shared/ui/buy-button";

export const ProductPage = () => {
    const { id } = useParams<{ id: string }>();
    const [product, setProduct] = useState<Product | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [quantity, setQuantity] = useState<number>(0);
    const [adding, setAdding] = useState<boolean>(false);

    useEffect(() => {
        if (!id) return;

        const fetchProduct = async () => {
            try {
                const data = await getProduct(Number(id));
                setProduct(data);
            } catch (e) {
                console.error(e);
                setError("Ошибка при загрузке товара");
            } finally {
                setLoading(false);
            }
        };

        fetchProduct();
    }, [id]);

    const handleAddToBasket = async () => {
        if (!product) return;

        setAdding(true);
        const user_id = 1;

        try {
            const success = await addProductToBasket(user_id, product.id, 1);
            if (success) {
                setQuantity(1);
            } else {
                alert("Не удалось добавить товар");
            }
        } catch (e) {
            console.error(e);
            alert("Ошибка при добавлении");
        } finally {
            setAdding(false);
        }
    };

    const handleIncrease = async () => {
        if (!product) return;

        const success = await increaseBasketQuantity(product.id);
        if (success) {
            setQuantity(prev => prev + 1);
        }
    };

    const handleDecrease = async () => {
        if (!product || quantity <= 0) return;

        const success = await decreaseBasketQuantity(product.id);
        if (success) {
            setQuantity(prev => Math.max(0, prev - 1));
        }
    };

    if (loading) return <p>Загрузка...</p>;
    if (error || !product) return <p>{error || "Товар не найден"}</p>;

    return (
        <div>
            <div className={styles.wrapper}>
                <img className={styles.productPhoto} src={product.photo || ProductImage} alt={product.name} />

                <div className={styles.productName}>{product.name}</div>

                <div className={styles.productDescription}>{product.description}</div>

                <div className={styles.productPrice}>{product.price.toLocaleString("ru-RU")} ₽</div>

                <BuyButton
                    productId={product.id}
                    userId={1}
                    initialQuantity={quantity}
                />
            </div>

            <TabBar />
        </div>
    );
};
