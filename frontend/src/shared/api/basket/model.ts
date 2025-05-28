import type { Product } from "../products/model";

export type Basket = {
    id: number;
    product: Product;
    user_id: number;
    quantity: number;
    created_at: Date;
    updated_at: Date;
}


export type AnswerAddBasket = {
    ok: boolean;
    message: string;
    basket_id: number
}


export type AnswerBaskets = {
    ok: boolean;
    message: string;
    baskets: Basket[]
}