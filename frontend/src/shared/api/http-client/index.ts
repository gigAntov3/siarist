import axios from "axios";

export const httpClient = axios.create({
    baseURL: "http://90.156.230.193/api",
})