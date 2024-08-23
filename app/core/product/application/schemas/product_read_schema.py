"""
Схема для получения информации о продукте.
"""

from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from app.core.product.domain.product_entity import Product
from app.core.product.domain.value_objects.product_category import ProductCategory


class ProductReadSchema(BaseModel):
    """
    Схема для получения информации о продукте.

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

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductReadSchema":
        """
        Создаёт схему с информацией о продукте.

        :param entity: Сущность продукта.
        :return: Схема с информацией о продукте.
        """
        return cls(
            uuid=entity.uuid.uuid,
            name=entity.name.name,
            category=entity.category,
            price=entity.price.price,
            available_count=entity.available_count.count
        )
