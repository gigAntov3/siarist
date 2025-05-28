import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import styles from './styles.module.css';

import { TabBar } from '../../shared/ui/tabbar';
import { Separator } from '../../shared/ui/separator';
import { BasketProductList } from '../../features/basket/ui/product-list';

import type { Basket } from '../../shared/api/basket/model';
import { getBaskets } from '../../shared/api/basket';
import { getUser } from '../../shared/api/users';

import { PaymentMethodModal } from '../../widgets/payment-method-modal';
import { EnterAccountModal } from '../../widgets/enter-account-modal';

export const BusketPage = () => {
  const [baskets, setBaskets] = useState<Basket[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [bonuses, setBonuses] = useState<number>(0);
  const [showDataModal, setShowDataModal] = useState(false);
  const [showPaymentModal, setShowPaymentModal] = useState(false);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [basketsData, userData] = await Promise.all([
          getBaskets(),
          getUser(1),
        ]);
        setBaskets(basketsData);
        setBonuses(userData.balance);
      } catch (err) {
        console.error(err);
        setError('Ошибка при загрузке данных');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
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

  const handleDataModalClose = () => {
    setShowDataModal(false);
  };

  const handlePaymentClick = () => {
    setShowPaymentModal(true);
  };

  const handlePaymentSelect = (method: string) => {
    setSelectedPaymentMethod(method);
    setShowPaymentModal(false);
    console.log('Выбран способ оплаты:', method);
    // Здесь можно выполнить финальную отправку данных
  };

  const handleDataModalSave = () => {
    setShowDataModal(false);
    setShowPaymentModal(true);
  };

  if (loading) return <div className={styles.wrapper}>Загрузка...</div>;
  if (error) return <div className={styles.wrapper}>{error}</div>;

  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>Корзина</div>

      {baskets.length === 0 ? (
        <div className={styles.emptyState}>
          <div className={styles.emptyTitle}>В корзине пока пусто</div>
          <div className={styles.emptySubtitle}>
            Загляните <Link to="/" className={styles.emptyLink}>на главную</Link> — собрали там товары,<br />
            которые могут вам понравиться
          </div>
        </div>
      ) : (
        <>
          <BasketProductList
            baskets={baskets}
            onQuantityChange={handleQuantityChange}
          />

          <Separator />

          <div className={styles.bonusWrapper}>
            <div className={styles.bonusInfo}>
              <div className={styles.bonusLabel}>Бонусы</div>
              <div className={styles.bonusAmount}>{bonuses.toLocaleString()} ₽</div>
            </div>
            <button className={styles.bonusButton}>Списать</button>
          </div>

          <hr className={styles.separator} />

          <div className={styles.totalWrapper}>
            <div className={styles.totalLabel}>Итого</div>
            <div className={styles.totalAmount}>
              {totalPrice.toLocaleString()} ₽
            </div>
          </div>

          <button className={styles.buyButton} onClick={() => setShowDataModal(true)}>
            Купить
          </button>

          {showDataModal && <EnterAccountModal
            onClose={handleDataModalClose}  // Закрытие без сохранения
            onSave={handleDataModalSave}    // Закрытие с сохранением, открыть окно оплаты
          />}
          {showPaymentModal && (
            <PaymentMethodModal
              onClose={() => setShowPaymentModal(false)}
              onSelect={handlePaymentSelect}
            />
          )}
        </>
      )}

      <TabBar />
    </div>
  );
};
