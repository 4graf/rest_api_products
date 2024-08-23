"""
ProductDao модель DAO для работы с продуктами в базе данных.
"""
import enum
from decimal import Decimal
from uuid import UUID

from sqlalchemy import String, Enum, Numeric, Integer
from sqlalchemy.orm import mapped_column, Mapped

from app.core.product.domain.product_entity import Product
from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_category import ProductCategory
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID
from app.core.shared_kernel.db.dao import BaseDao


class ProductDao(BaseDao):
    """
    Модель DAO для работы с продуктами в базе данных.

    :cvar __tablename__: Название таблицы в базе данных.
    :cvar id: Уникальный идентификатор продукта, первичный ключ.
    :cvar name: Наименование продукта.
    :cvar category: Категория продукта.
    :cvar price: Цена продукта за 1 единицу.
    :cvar available_count: Доступное количество продукта в штуках или килограммах.
    """

    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    category: Mapped[enum.Enum] = mapped_column(Enum(ProductCategory))
    price: Mapped[Decimal] = mapped_column(Numeric(11, 2), default="0")
    available_count: Mapped[int] = mapped_column(Integer, default="0")

    def to_entity(self) -> Product:
        """
        Создаёт сущность продукта из модели DAO.

        :return: Созданная сущность продукта.
        """

        return Product(
            uuid=ProductUUID(self.id),
            name=ProductName(self.name),
            category=ProductCategory(self.category),
            price=Price(self.price),
            available_count=ProductCount(self.available_count)
        )

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductDao":
        """
        Создаёт модель DAO из сущности продукта.

        :param entity: Сущность продукта.
        :return: Созданная модель DAO продукта.
        """

        return cls(
            id=entity.uuid.uuid,
            name=entity.name.name,
            category=entity.category,
            price=entity.price.price,
            available_count=entity.available_count.count
        )
