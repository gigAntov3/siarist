import { httpClient } from "../http-client";
import type { User, AnswerUser } from "./model";



export const getUser = async (user_id: number): Promise<User> => {
    const response = await httpClient.get<AnswerUser>(`users/${user_id}`);
    return response.data.user;
};