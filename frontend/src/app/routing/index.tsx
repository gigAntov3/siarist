import { createBrowserRouter } from "react-router-dom";
import { MainLayout } from "../../shared/ui/main-layout";
import { HomePage } from "../../pages/home-page";
import { ProductPage } from "../../pages/product-page";
import { FeedbackPage } from "../../pages/feedback-page";
import { BusketPage } from "../../pages/basket-page";
import { BonusPage } from "../../pages/bonus-page";
import { PaymentStatusPage } from "../../pages/payment-status-page";


export const router = createBrowserRouter([
    {
        path: "/",
        element: <MainLayout />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: "product/:id",
                element: <ProductPage />,
            },
            {
                path: "feedback",
                element: <FeedbackPage />,
            },
            {
                path: "busket",
                element: <BusketPage />,
            },
            {
                path: "bonus",
                element: <BonusPage />,
            },
            {
                path: "payments",
                element: <PaymentStatusPage />,
            },
        ],
    },
]);