"""
Исключения для цены продукта в доменном слое.
"""

from app.core.product.domain.exceptions.base_product_exceptions import ProductValidationException


class ProductPriceLessThanZeroError(ProductValidationException):
    """
    Исключение, возникающее при цене продукта меньше 0.
    """
    def __init__(self, msg: str = 'Цена продукта не должна быть меньше 0'):
        """
        Конструктор ProductPriceLessThanZeroError.

        :param msg: Сообщение исключения.
        """
        super().__init__(msg)
