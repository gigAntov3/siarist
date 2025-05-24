import { createBrowserRouter } from "react-router-dom";
import { MainLayout } from "../../shared/ui/main-layout";
import { HomePage } from "../../pages/home-page";
import { ProductPage } from "../../pages/product-page";
import { FeedbackPage } from "../../pages/feedback-page";
import { BusketPage } from "../../pages/basket-page";
import { BonusPage } from "../../pages/bonus-page";
import { PaymentStatusPage } from "../../pages/payment-status-page";
import { EnterDataPage } from "../../pages/enter-data-page";


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
                path: "product",
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
                path: "payment-status",
                element: <PaymentStatusPage />,
            },
            {
                path: "enter-data",
                element: <EnterDataPage />,
            }
        ],
    },
]);