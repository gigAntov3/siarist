import ProductImage from '../assets/product.png';
import { useEffect, useState } from "react";
import styles from './product-list.module.css';
import type { Product } from "../../../shared/api/products/model";
import { getProducts } from "../../../shared/api/products";
import { ProductCard } from './product-card';

type Tag = 'new' | 'best' | 'hit';

const isTag = (tag: string): tag is Tag => {
  return ['new', 'best', 'hit'].includes(tag);
};

type Props = {
  title: string;
  category_id: number;
};

export const ProductList = ({ title, category_id }: Props) => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      setError(null);
      try {
        const result = await getProducts(category_id, 10, 0);
        setProducts(result);
      } catch (e) {
        console.error(e);
        setError("Ошибка при загрузке товаров");
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [category_id]);

  return (
    <div className={styles.wrapper}>
      <span className={styles.categoryTitle}>{title}</span>

      {loading && <p>Загрузка...</p>}
      {error && <p>{error}</p>}

      <div className={styles.productsList}>
        {products.map(product => {
          const tag = isTag(product.tag) ? product.tag : undefined;

          return (
            <ProductCard
              key={product.id}
              id={product.id}
              name={product.name}
              price={product.price}
              image={product.photo || ProductImage}
              tag={tag}
            />
          );
        })}
      </div>
    </div>
  );
};