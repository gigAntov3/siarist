import { httpClient } from "../http-client";
import type { Product, AnswerProduct, AnswerProducts } from "./model";



export const getProducts = async (category_id: number | null, limit = 10, offset = 0): Promise<Product[]> => {
    const response = await httpClient.get<AnswerProducts>("products", {
        params: { category_id, limit, offset },
    });

    return response.data.products;
};


export const getProduct = async (id: number): Promise<Product> => {
    const response = await httpClient.get<AnswerProduct>(`products/${id}`);

    return response.data.product;
};