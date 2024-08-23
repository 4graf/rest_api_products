"""
API-маршруты для работы с продуктами.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from app.api.http_errors import ResourceNotFoundError, ResourceExistsError, RequestParamValidationError
from app.api.product.dependencies import get_product_service
from app.core.product.application.exceptions import ProductNotFoundException, ProductExistsException
from app.core.product.application.schemas.product_create_schema import ProductCreateSchema
from app.core.product.application.schemas.product_read_schema import ProductReadSchema
from app.core.product.application.schemas.product_update_schema import ProductUpdateSchema
from app.core.product.application.services.product_service import ProductService
from app.core.product.domain.exceptions.base_product_exceptions import ProductValidationException
from app.core.product.domain.utils.product_filter_params import ProductFilterParams

product_router = APIRouter(prefix='/products', tags=['Product'])


@product_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[ProductReadSchema]
)
async def get_all_products(product_service: Annotated[ProductService, Depends(get_product_service)],
                           product_filter_params: ProductFilterParams = Depends()) -> list[ProductReadSchema]:
    """
    Маршрут для получения всех продуктов.

    :param product_filter_params: Параметры фильтрации продуктов.
    :param product_service: Сервис для работы с продуктами.
    :return: Список продуктов.
    """
    products = await product_service.get_all_products(product_filter_params=product_filter_params)
    return products


@product_router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductReadSchema
)
async def get_product_by_id(id: UUID,
                            product_service: Annotated[ProductService, Depends(get_product_service)])\
        -> ProductReadSchema:
    """
    Маршрут для получения продукта по его идентификатору.

    :param id: Уникальный идентификатор продукта.
    :param product_service: Сервис для работы с продуктами.
    :return: Продукт.
    """
    try:
        product = await product_service.get_product_by_id(id)
    except ProductNotFoundException as exc:
        raise ResourceNotFoundError(exception_msg=str(exc)) from exc

    return product


@product_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductReadSchema
)
async def add_product(product_to_add: ProductCreateSchema,
                      product_service: Annotated[ProductService, Depends(get_product_service)]) -> ProductReadSchema:
    """
    Маршрут для добавления продукта.

    :param product_to_add: Информация о продукте.
    :param product_service: Сервис для работы с продуктами.
    :return: Добавленный продукт.
    """
    try:
        added_product = await product_service.add_product(product_to_add)
    except ProductValidationException as exc:
        raise RequestParamValidationError(exception_msg=str(exc)) from exc
    except ProductExistsException as exc:
        raise ResourceExistsError(exception_msg=str(exc)) from exc
    return added_product


@product_router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductReadSchema
)
async def update_product(id: UUID,
                         product_to_update: ProductUpdateSchema,
                         product_service: Annotated[ProductService, Depends(get_product_service)]) -> ProductReadSchema:
    """
    Маршрут для обновления продукта по его идентификатору.

    :param id: Уникальный идентификатор продукта.
    :param product_to_update: Новая информация о продукте.
    :param product_service: Сервис для работы с продуктами.
    :return: Обновлённый продукт.
    """

    try:
        updated_product = await product_service.update_product(id_=id, data=product_to_update)
    except ProductValidationException as exc:
        raise RequestParamValidationError(exception_msg=str(exc)) from exc
    except ProductNotFoundException as exc:
        raise ResourceNotFoundError(exception_msg=str(exc)) from exc
    except ProductExistsException as exc:
        raise ResourceExistsError(exception_msg=str(exc)) from exc
    return updated_product


@product_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product_by_id(id: UUID,
                               product_service: Annotated[ProductService, Depends(get_product_service)]) -> None:
    """
    Маршрут для удаления продукта по его идентификатору.

    :param id: Уникальный идентификатор продукта.
    :param product_service: Сервис для работы с продуктами.
    """

    try:
        await product_service.delete_product_by_id(id)
    except ProductValidationException as exc:
        raise RequestParamValidationError(exception_msg=str(exc)) from exc
    except ProductNotFoundException as exc:
        raise ResourceNotFoundError(exception_msg=str(exc)) from exc
