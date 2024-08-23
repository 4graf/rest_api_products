"""
Схема для обновления продукта.
"""

from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from app.core.product.domain.value_objects.product_category import ProductCategory


class ProductUpdateSchema(BaseModel):
    """
    Схема для обновления продукта.

    :ivar uuid: Уникальный идентификатор продукта.
    :ivar name: Наименование продукта.
    :ivar category: Категория продукта.
    :ivar price: Цена продукта за 1 единицу.
    :ivar available_count: Доступное количество продукта в штуках или килограммах.
    """

    uuid: UUID
    name: str
    category: ProductCategory
    price: Decimal
    available_count: int
