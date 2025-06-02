import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import styles from './styles.module.css';

import { TabBar } from '../../shared/ui/tabbar';
import { Separator } from '../../shared/ui/separator';
import { BasketProductList } from '../../features/basket/ui/product-list';

import type { Basket } from '../../shared/api/basket/model';
import { deleteBaskets, getBaskets } from '../../shared/api/basket';
import { getUser } from '../../shared/api/users';

import { PaymentMethodModal } from '../../widgets/payment-method-modal';
import { EnterAccountModal } from '../../widgets/enter-account-modal';
import { addOrder } from '../../shared/api/orders';
import { getPaymentLink } from '../../shared/api/payments';

export const BusketPage = () => {
  const [baskets, setBaskets] = useState<Basket[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [bonuses, setBonuses] = useState<number>(0);
  const [bonusesToUse, setBonusesToUse] = useState(0);
  const [showDataModal, setShowDataModal] = useState(false);
  const [showPaymentModal, setShowPaymentModal] = useState(false);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState<string | null>(null);
  const [platform, setPlatform] = useState("Google Play");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const [order, setOrder] = useState<any>(null);

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
    setBaskets((prev) => {
      if (newQuantity === 0) {
        // Удаляем товар, если количество стало 0
        return prev.filter((item) => item.id !== basketId);
      }

      // Иначе обновляем количество
      return prev.map((item) =>
        item.id === basketId ? { ...item, quantity: newQuantity } : item
      );
    });
  };

  const totalPrice = baskets.reduce(
    (acc, basket) => acc + basket.quantity * basket.product.price,
    0
  );
  const totalPriceAfterBonuses = Math.max(totalPrice - bonusesToUse, 0);

  const handleDataModalClose = () => {
    setShowDataModal(false);
  };

  const handleUseBonuses = () => {
    if (bonusesToUse > 0) {
      setBonusesToUse(0); // отмена списания
    } else {
      const maxBonuses = Math.min(bonuses, totalPrice);
      setBonusesToUse(maxBonuses);
    }
  };

  const handlePaymentSelect = async (method: string) => {
    setSelectedPaymentMethod(method);
    setShowPaymentModal(false);

    if (!email || !password || !username || baskets.length === 0) return;

    const orderData = {
      user_id: 1,
      order_products: baskets.map((basket) => ({
        product_id: basket.product.id,
        quantity: basket.quantity,
      })),
      withdrawn_bonuses: bonusesToUse,
      total_amount: totalPriceAfterBonuses,
      platform,
      email,
      password,
      nickname: username,
      status: 'new',
      payment_method: method,
      payment_status: 'pending',
    };

    try {
      const order_id = await addOrder(orderData);

      setOrder(order_id);

      const ipResponse = await fetch('https://api.ipify.org?format=json');
      const ipData = await ipResponse.json();
      const ip = ipData.ip;

      if (order_id === null) throw new Error("Order ID is null");

      const paymentLink = await getPaymentLink(method, order_id, totalPriceAfterBonuses, email, ip);
      console.log('paymentLink:', paymentLink);

      await deleteBaskets(1);
      
      window.location.replace(paymentLink);
    } catch (err) {
      console.error('Ошибка при создании заказа или получении ссылки на оплату:', err);
      setError('Ошибка при создании заказа');
    }
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
            <button
              className={styles.bonusButton}
              onClick={handleUseBonuses}
              disabled={bonuses === 0 || totalPrice === 0}
            >
              {bonusesToUse > 0 ? 'Отменить' : 'Списать'}
            </button>
          </div>

          <hr className={styles.separator} />

          <div className={styles.totalWrapper}>
            <div className={styles.totalLabel}>Итого</div>
            <div className={styles.totalAmount}>
              {totalPriceAfterBonuses.toLocaleString()} ₽
            </div>
          </div>

          <button className={styles.buyButton} onClick={() => setShowDataModal(true)}>
            Купить
          </button>

          {showDataModal && (
            <EnterAccountModal
              onClose={handleDataModalClose}
              onSave={handleDataModalSave}
              platform={platform}
              setPlatform={setPlatform}
              email={email}
              setEmail={setEmail}
              password={password}
              setPassword={setPassword}
              username={username}
              setUsername={setUsername}
            />
          )}
          {showPaymentModal && (
            <PaymentMethodModal
              onClose={() => setShowPaymentModal(false)}
              onSelect={handlePaymentSelect}
              selectedMethod={selectedPaymentMethod}
              setSelectedMethod={setSelectedPaymentMethod}
            />
          )}
        </>
      )}

      <TabBar />
    </div>
  );
};
