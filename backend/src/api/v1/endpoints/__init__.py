from fastapi import APIRouter

from .products import router as products_router
from .categories import router as categories_router
from .users import router as users_router
from .feedbacks import router as feedbacks_router
from .basket import router as basket_router
from .files import router as files_router
from .orders import router as orders_router
from .payments import router as payments_router

router = APIRouter()

router.include_router(products_router)
router.include_router(categories_router)
router.include_router(users_router)
router.include_router(feedbacks_router)
router.include_router(basket_router)
router.include_router(files_router)
router.include_router(orders_router)
router.include_router(payments_router)