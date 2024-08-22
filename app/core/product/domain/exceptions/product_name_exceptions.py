"""
Исключения для наименования продукта в доменном слое.
"""

from app.core.product.domain.exceptions.base_product_exceptions import ProductValidationException


class MinLengthProductNameError(ProductValidationException):
    """
    Исключение, возникающее при длине наименования продукта меньшей минимальной.
    """
    def __init__(self, msg: str = 'Длина наименования продукта меньше минимальной', min_length: int = None):
        """
        Конструктор MinLengthProductNameError.

        :param msg: Сообщение исключения.
        :param min_length: Минимальная длина для наименования продукта.
        """
        if min_length:
            msg = f'{msg} [{min_length}]'
        super().__init__(msg)


class MaxLengthProductNameError(ProductValidationException):
    """
    Исключение, возникающее при длине наименования продукта большей максимальной.
    """
    def __init__(self, msg: str = 'Длина наименования продукта больше максимальной', max_length: int = None):
        """
        Конструктор MaxLengthProductNameError.

        :param msg: Сообщение исключения.
        :param max_length: Максимальная длина для наименования продукта.
        """
        if max_length:
            msg = f'{msg} [{max_length}]'
        super().__init__(msg)
