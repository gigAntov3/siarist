import { httpClient } from "../http-client";
import type { Answer } from "../http-client/model";
import type { Basket, AnswerBaskets } from "./model";


export const getBaskets = async (): Promise<Basket[]> => {
    const response = await httpClient.get<AnswerBaskets>("basket");
    return response.data.baskets;
};


export const increaseBasketQuantity = async (id: number): Promise<Boolean> => {
    const response = await httpClient.post<Answer>(`basket/${id}/increase`);
    return response.data.ok;
}


export const decreaseBasketQuantity = async (id: number): Promise<Boolean> => {
    const response = await httpClient.post<Answer>(`basket/${id}/decrease`);
    return response.data.ok;
}