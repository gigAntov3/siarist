export type Category = {
    id: number;
    name: string;
}


export type AnswerCategories = {
    ok: boolean;
    message: string;
    categories: Category[];
}