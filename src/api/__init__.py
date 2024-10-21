from fastapi import APIRouter
from api.routes.products import router as products_router
from api.routes.product_categories import router as product_categories_router

router = APIRouter()
router.include_router(products_router)
router.include_router(product_categories_router)
