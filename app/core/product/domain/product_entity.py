"""
Сущность продукта.
"""
import copy
from dataclasses import dataclass, field

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

    :ivar uuid: Уникальный идентификатор продукта.
    :ivar name: Наименование продукта.
    :ivar category: Категория продукта.
    :ivar price: Цена продукта за 1 единицу.
    :ivar available_count: Доступное количество продукта в штуках или килограммах.
    """

    uuid: ProductUUID
    name: ProductName
    category: ProductCategory
    price: Price = field(default_factory=lambda: copy.deepcopy(Price(Decimal(0))))
    available_count: ProductCount = field(default_factory=lambda: copy.deepcopy(ProductCount(0)))
