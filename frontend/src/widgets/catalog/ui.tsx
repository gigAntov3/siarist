import { useEffect, useState } from 'react';

import { getCategories } from '../../shared/api/categories';
import type { Category } from '../../shared/api/categories/model'; // Импортируем тип Category

import { ProductList } from '../../features/products/ui/product-list';
import { Separator } from '../../shared/ui/separator';

import styles from './styles.module.css';

export const Catalog = () => {
    const [categories, setCategories] = useState<Category[]>([]);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const data = await getCategories();
                setCategories(data);
            } catch (error) {
                console.error('Ошибка при загрузке категорий:', error);
            }
        };

        fetchCategories();
    }, []);

    return (
        <div className={styles.catalog}>
            {categories.map((category, index) => (
                <div className={styles.category} key={category.id}>
                    <ProductList title={category.name} category_id={category.id} />
                    {index < categories.length - 1 && <Separator />}
                </div>
            ))}
        </div>
    );
};
