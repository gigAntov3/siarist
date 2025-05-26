import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import styles from './styles.module.css';

import PlusIcon from './assets/plus.svg?react';
import MinusIcon from './assets/minus.svg?react';
import ProductImage from './assets/product.png';

import { TabBar } from '../../shared/ui/tabbar';
import { Separator } from '../../shared/ui/separator';
import { BasketProductList } from '../../features/basket/ui/product-list';

import type { Basket } from '../../shared/api/basket/model';
import { getBaskets } from '../../shared/api/basket';

export const BusketPage = () => {
  const [baskets, setBaskets] = useState<Basket[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchBaskets = async () => {
      try {
        const data = await getBaskets();
        setBaskets(data);
      } catch (err) {
        console.error(err);
        setError('Ошибка при загрузке корзины');
      } finally {
        setLoading(false);
      }
    };

    fetchBaskets();
  }, []);

  const handleQuantityChange = (basketId: number, newQuantity: number) => {
    setBaskets((prev) =>
      prev.map((item) =>
        item.id === basketId ? { ...item, quantity: newQuantity } : item
      )
    );
  };

  const totalPrice = baskets.reduce(
    (acc, basket) => acc + basket.quantity * basket.product.price,
    0
  );

  if (loading) return <div className={styles.wrapper}>Загрузка...</div>;
  if (error) return <div className={styles.wrapper}>{error}</div>;

  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>Корзина</div>

      <BasketProductList baskets={baskets} onQuantityChange={handleQuantityChange} />

      <Separator />

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
        <div className={styles.totalAmount}>{totalPrice.toLocaleString()} ₽</div>
      </div>

      <Link to={'/enter-data'}>
        <button className={styles.buyButton}>Купить</button>
      </Link>

      <TabBar />
    </div>
  );
};