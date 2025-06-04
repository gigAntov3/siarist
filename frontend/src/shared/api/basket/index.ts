import { httpClient } from "../http-client";
import type { Answer } from "../http-client/model";
import type { Basket, AnswerAddBasket, AnswerBaskets } from "./model";


export const getBaskets = async (): Promise<Basket[]> => {
    const response = await httpClient.get<AnswerBaskets>("basket");
    return response.data.baskets;
};


export const addProductToBasket = async (user_id: number, product_id: number, quantity: number): Promise<number | null> => {
    const response = await httpClient.post<AnswerAddBasket>(`basket`, { user_id, product_id, quantity });
    return response.data.basket_id;
}


export const increaseBasketQuantity = async (id: number): Promise<boolean> => {
    const response = await httpClient.post<Answer>(`basket/${id}/increase`);
    return response.data.ok;
}


export const decreaseBasketQuantity = async (id: number): Promise<boolean> => {
    const response = await httpClient.post<Answer>(`basket/${id}/decrease`);
    return response.data.ok;
}


export const deleteBaskets = async (user_id: number): Promise<boolean> => {
    const response = await httpClient.delete<Answer>(`basket/`, { params: { user_id } });
    return response.data.ok;
}


export const deleteBasket = async (id: number): Promise<boolean> => {
    const response = await httpClient.delete<Answer>(`basket/${id}`);
    return response.data.ok;
}