import { httpClient } from "../http-client";
import type { AnswerPaymentLink } from "./model";

export const getPaymentLink = async (method: string, order_id: number, amount: number, email: string, ip: string): Promise<string> => {
    const response = await httpClient.get<AnswerPaymentLink>(`payments`,
        {
            params: { method, order_id, amount, email, ip, currency: "RUB" },
        }
    );
    return response.data.url;
};