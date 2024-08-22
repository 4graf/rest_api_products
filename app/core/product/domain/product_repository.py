"""
Интерфейс репозитория для сущности продуктов ProductRepository.
"""

from abc import ABC, abstractmethod
from typing import Sequence

from app.core.product.domain.utils.product_filter_params import ProductFilterParams

from app.core.product.domain.product_entity import Product
from app.core.shared_kernel.domain.repository import BaseRepository


class ProductRepository(BaseRepository[Product], ABC):
    """
    Интерфейс репозитория для сущности продуктов.
    """

    @abstractmethod
    async def get_by_filter(self, product_filter_params: ProductFilterParams) -> Sequence[Product]:
        """
        Получает сущность продукта по фильтру.

        :param product_filter_params: Параметры фильтра.
        :return: Список отфильтрованных продуктов.
        """
        ...
