"""
Реализация репозитория базы данных для продуктов ProductDBRepository.
"""
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.core.product.domain.product_entity import Product
from app.core.product.domain.product_repository import ProductRepository
from app.core.product.domain.utils.product_filter_params import ProductFilterParams
from app.core.product.infrastructure.models.product_dao import ProductDao
from app.core.product.infrastructure.repositories.utils.product_filter import ProductFilter
from app.core.shared_kernel.db.repository import BaseDBRepository


class ProductDBRepository(ProductRepository, BaseDBRepository[Product]):
    """
    Реализация репозитория базы данных для продуктов.

    :cvar dao: DAO модель для работы с продуктами в базе данных.
    """
    @property
    def dao(self) -> type[ProductDao]:
        return ProductDao

    async def get_by_filter(self, product_filter_params: ProductFilterParams) -> list[Product]:
        """
        Получает сущность продукта по фильтру.

        :param product_filter_params: Параметры фильтра.
        :return: Список отфильтрованных продуктов.
        """
        get_query = select(self.dao)
        filter_query = ProductFilter.filter_query(query=get_query, product_filter_params=product_filter_params)
        try:
            result = await self.session.execute(filter_query)
            result = result.scalars().all()
        except NoResultFound:
            return []
        return [dao.to_entity() for dao in result]
