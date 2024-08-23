"""
Функции для получения зависимостей продуктов.
Включает в себя создание сервиса продуктов.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.product.application.services.product_service import ProductService
from app.core.product.infrastructure.repositories.product_repository import ProductDBRepository
from app.core.shared_kernel.db.dependencies import get_async_db_session


async def get_product_service(session: AsyncSession = Depends(get_async_db_session)) -> ProductService:
    """
    Получает сервис продуктов.

    :param session: Асинхронная сессия базы данных.
    :return: Сервис продуктов.
    """

    product_repository = ProductDBRepository(session)
    return ProductService(product_repository=product_repository)
