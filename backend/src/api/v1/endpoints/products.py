from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas.products import (
    ProductSchema,
    AnswerProductSchema,
    ProductAddSchema,
    AnswerProductAddSchema,
    AnswerProductsSchema,
    ProductUpdateSchema,
    AnswerProductUpdateSchema,
    AnswerProductDeleteSchema,
)

from services.products import ProductsService

from api.v1.dependencies.products import products_service


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("")
async def add_profile(
    product: ProductAddSchema,
    products_service: Annotated[ProductsService, Depends(products_service)]
) -> AnswerProductAddSchema:
    product_id = await products_service.add_product(product)
    return AnswerProductAddSchema(ok=True, message="Product added successfully", product_id=product_id)


@router.get("")
async def get_profiles(
    products_service: Annotated[ProductsService, Depends(products_service)],
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
) -> AnswerProductsSchema:
    products = await products_service.get_products(limit=limit, offset=offset)
    return AnswerProductsSchema(ok=True, message="Products retrieved successfully", products=products)


@router.get("/{product_id}")
async def get_profile(
    product_id: int,
    products_service: Annotated[ProductsService, Depends(products_service)],
) -> AnswerProductSchema:
    product = await products_service.get_product(product_id)
    return AnswerProductSchema(ok=True, message="Product retrieved successfully", product=product)


@router.patch("/{product_id}")
async def update_profile(
    product_id: int,
    product: ProductUpdateSchema,
    products_service: Annotated[ProductsService, Depends(products_service)],
) -> AnswerProductUpdateSchema:
    product = await products_service.update_product(product_id, product)
    return AnswerProductUpdateSchema(ok=True, message="Product updated successfully")


@router.delete("/{product_id}")
async def delete_profile(
    product_id: int,
    products_service: Annotated[ProductsService, Depends(products_service)],
) -> AnswerProductDeleteSchema:
    await products_service.delete_product(product_id)
    return AnswerProductDeleteSchema(ok=True, message="Product deleted successfully")
