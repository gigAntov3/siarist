import { httpClient } from "../http-client";
import type { Category, AnswerCategories } from "./model";



export const getCategories = async (limit = 10, offset = 0): Promise<Category[]> => {
    const response = await httpClient.get<AnswerCategories>("categories", {
        params: { limit, offset },
    });

    return response.data.categories;
};