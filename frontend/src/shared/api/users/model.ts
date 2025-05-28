export type User = {
    id: number;
    chat_id: string;
    first_name: string;
    last_name: string;
    username: string;
    balance: number;
    purchases_count: number;
    created_at: string;
    updated_at: string;
}

export type AnswerUser = {
    ok: boolean;
    message: string;
    user: User;
}