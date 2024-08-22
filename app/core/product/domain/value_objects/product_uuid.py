"""
Объект значение уникального идентификатора продукта.
"""

from dataclasses import dataclass
from uuid import UUID

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError


@dataclass(slots=True)
class ProductUUID:
    """
    Объект значение уникального идентификатора продукта.

    :ivar uuid: Уникальный идентификатор продукта.
    """

    uuid: UUID

    def __post_init__(self):
        """
        Проверяет идентификатор на тип данных
        """
        if not isinstance(self.uuid, UUID):
            raise ProductTypeError(extra_msg_exception='Идентификатор продукта должен быть типом `UUID`')
