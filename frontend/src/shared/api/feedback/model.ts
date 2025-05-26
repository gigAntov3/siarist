import type { User } from "../users/model";


export type Feedback = {
    id: number
    content: string
    priority: number
    author: User
    created_at: Date
    updated_at: Date
}


export type AnswerFeedbacks = {
    ok: boolean
    message: string
    feedbacks: Feedback[]
}


