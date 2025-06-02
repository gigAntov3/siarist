import { httpClient } from "../http-client";
import type { Feedback, AnswerFeedbacks, AnswerFeedbacksCount } from "./model";



export const getFeedbacks = async (limit = 10, offset = 0): Promise<Feedback[]> => {
    const response = await httpClient.get<AnswerFeedbacks>("feedbacks", {
        params: { limit, offset },
    });

    return response.data.feedbacks;
};


export const getFeedbacksCount = async (): Promise<number> => {
    const response = await httpClient.get<AnswerFeedbacksCount>("feedbacks/count");
    return response.data.count;
};