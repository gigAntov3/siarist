import axios from "axios";

export const httpClient = axios.create({
    baseURL: "http://corrdev.ru/api",
})