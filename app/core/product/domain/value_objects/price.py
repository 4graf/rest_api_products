"""
Объект значение цены.
"""

from dataclasses import dataclass

from decimal import Decimal
from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_price_exceptions import ProductPriceLessThanZeroError


@dataclass(slots=True)
class Price:
    """
    Объект значение цены.

    :ivar price: Цена.
    """

    price: Decimal = Decimal(0)

    def __post_init__(self):
        """
        Проверяет цену на тип данных и корректность.
        """
        if not isinstance(self.price, Decimal):
            raise ProductTypeError(extra_msg_exception='Цена должна быть типа `Decimal`')
        if self.price < 0:
            raise ProductPriceLessThanZeroError()
