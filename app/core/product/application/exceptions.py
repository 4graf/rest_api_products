"""
Исключения для продуктов в слое приложения.
"""
from app.core.product.domain.exceptions.base_product_exceptions import ProductException


class ProductNotFoundException(ProductException):
    """
    Исключение, возникающее если продукт не был найден.
    """

    def __init__(self, msg: str = 'Продукт не был найден'):
        """
        Конструктор ProductNotFoundException.

        :param msg: Сообщение исключения.
        """
        super().__init__(msg)


class ProductExistsException(ProductException):
    """
    Исключение, возникающее если добавленный продукт уже существует.
    """

    def __init__(self, msg: str = 'Продукт уже существует'):
        """
        Конструктор ProductExistsException.

        :param msg: Сообщение исключения.
        """
        super().__init__(msg)
