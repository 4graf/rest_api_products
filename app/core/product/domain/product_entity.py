"""
Сущность продукта.
"""

from dataclasses import dataclass

from decimal import Decimal

from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_category import ProductCategory
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID
from app.core.shared_kernel.domain.entity import BaseEntity


@dataclass(slots=True, eq=False)
class Product(BaseEntity):
    """
    Представляет сущность продукта и его бизнес-логику.

    :cvar uuid: Уникальный идентификатор продукта.
    :cvar name: Наименование продукта.
    :cvar category: Категория продукта.
    :cvar price: Цена продукта за 1 единицу.
    :cvar available_count: Доступное количество продукта в штуках или килограммах.
    """

    uuid: ProductUUID
    name: ProductName
    category: ProductCategory
    price: Price = Price(Decimal(0))
    available_count: ProductCount = ProductCount(0)
