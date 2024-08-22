"""
Исключения для количества продукта в доменном слое.
"""

from app.core.product.domain.exceptions.base_product_exceptions import ProductValidationException


class ProductCountLessThanZeroError(ProductValidationException):
    """
    Исключение, возникающее при количестве продуктов меньше 0.
    """
    def __init__(self, msg: str = 'Количество продукта не должно быть меньше 0'):
        """
        Конструктор ProductCountLessThanZeroError.

        :param msg: Сообщение исключения.
        """
        super().__init__(msg)
