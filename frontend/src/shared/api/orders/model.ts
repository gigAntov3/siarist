import type { Product } from "../products/model"
import type { User } from "../users/model"


export type OrderProduct = {
    id: number,
    quantity: number,
    product: Product
}

export type Order = {
    id: number,
    user: User
    order_products: OrderProduct[],
    withdrawn_bonuses: number | null,
    total_amount: number,
    platform: string,
    email: string,
    password: string | null,
    nickname: string,
    status: string,
    payment_method: string,
    payment_status: string | null,
    created_at: Date,
    updated_at: Date
}


export type AnswerOrder = {
    ok: boolean,
    message: string
    order: Order
}


export type AnswerOrders = {
    ok: boolean,
    message: string
    orders: Order[]
}


export type OrderAddProduct = {
    quantity: number,
    product_id: number
}


export type OrderAdd = {
    user_id: number,
    order_products: OrderAddProduct[],
    withdrawn_bonuses: number,
    total_amount: number,
    platform: string,
    email: string,
    password: string,
    nickname: string,
    status: string,
    payment_method: string,
    payment_status: string,
}


export type AnswerAddOrder = {
    ok: boolean,
    message: string
    order_id: number
}