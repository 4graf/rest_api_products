"""
Схема для создания нового продукта.
"""

from decimal import Decimal

from pydantic import BaseModel

from app.core.product.domain.value_objects.product_category import ProductCategory


class ProductCreateSchema(BaseModel):
    """
    Схема для создания нового продукта.

    :ivar name: Наименование продукта.
    :ivar category: Категория продукта.
    :ivar price: Цена продукта за 1 единицу.
    :ivar available_count: Доступное количество продукта в штуках или килограммах.
    """
    name: str
    category: ProductCategory
    price: Decimal
    available_count: int
