import { httpClient } from "../http-client";
import type { Order, AnswerOrders, AnswerAddOrder, OrderAdd} from "./model";


export const getOrders = async (limit = 10, offset = 0): Promise<Order[]> => {
    const response = await httpClient.get<AnswerOrders>("orders", {
        params: { limit, offset },
    });

    return response.data.orders;
};


export const addOrder = async (orderData: OrderAdd): Promise<number | null> => {
  console.log(orderData);
  const response = await httpClient.post<AnswerAddOrder>('orders', orderData);
  return response.data.order_id;
};