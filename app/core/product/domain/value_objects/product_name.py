"""
Объект значение наименования продукта.
"""

from dataclasses import dataclass

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_name_exceptions import MinLengthProductNameError, \
    MaxLengthProductNameError


@dataclass(slots=True)
class ProductName:
    """
    Объект значение наименования продукта с валидацией

    :ivar name: Наименование продукта.
    """

    name: str

    def __post_init__(self):
        """
        Проверяет наименование на тип данных и длину
        """
        if not isinstance(self.name, str):
            raise ProductTypeError(extra_msg_exception='Наименование продукта должно быть типом `str`')
        if len(self.name) < 5:
            raise MinLengthProductNameError(min_length=5)
        if len(self.name) > 500:
            raise MaxLengthProductNameError(max_length=500)
