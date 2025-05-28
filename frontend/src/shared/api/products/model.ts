export type Product = {
    id: number;
    name: string;
    description: string;
    price: number;
    tag: string;
    photo: string;
    category_id: number;
    created_at: string;
    updated_at: string;
}


export type AnswerProduct = {
    ok: boolean;
    message: string;
    product: Product;
}


export type AnswerProducts = {
    ok: boolean;
    message: string;
    products: Product[];
}