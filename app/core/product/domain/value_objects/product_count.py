"""
Объект значение количества продукта.
"""

from dataclasses import dataclass

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_count_exceptions import ProductCountLessThanZeroError


@dataclass(slots=True)
class ProductCount:
    """
    Объект значение количества продукта.

    :ivar count: Количество продукта в штуках.
    """

    count: int

    def __post_init__(self):
        """
        Проверяет количество на тип данных и корректность.
        """
        if not isinstance(self.count, int):
            raise ProductTypeError(extra_msg_exception='Количество продукта должно быть типа `int`')
        if self.count < 0:
            raise ProductCountLessThanZeroError()
