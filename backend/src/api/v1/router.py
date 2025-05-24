from fastapi import APIRouter

from .endpoints import router as endpoints

router = APIRouter()
router.include_router(endpoints)