"""
Объект значение цены.
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_UP

from _decimal import Context

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_price_exceptions import ProductPriceLessThanZeroError, \
    MaxValueProductPriceError


@dataclass(slots=True)
class Price:
    """
    Объект значение цены.

    :ivar price: Цена.
    """

    price: Decimal | int | float | str

    def __post_init__(self):
        """
        Проверяет цену на тип данных и корректность.
        """
        try:
            self.price = Decimal(str(self.price)).quantize(Decimal('0.01'), rounding=ROUND_UP)
        except InvalidOperation:
            raise ProductTypeError(extra_msg_exception='Цена должна быть числом')

        if self.price < 0:
            raise ProductPriceLessThanZeroError()
        if self.price > 1_000_000_000:
            raise MaxValueProductPriceError(max_price=1_000_000_000)
