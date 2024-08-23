"""
Юнит-тесты объекта значения ProductName.
"""

import pytest

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_name_exceptions import MinLengthProductNameError, \
    MaxLengthProductNameError
from app.core.product.domain.value_objects.product_name import ProductName


class TestProductName:
    """
    Юнит-тесты для объекта значения :class:`ProductName`
    """

    def test_create_valueobject_productname(self):
        """
        Проверяет корректное создание объекта значения наименования продукта.
        """
        name_default = 'Велосипед'
        name_min = 'В'*100
        name_max = 'В'*3
        product_name_default = ProductName(name=name_default)
        product_name_min = ProductName(name=name_min)
        product_name_max = ProductName(name=name_max)

        assert product_name_default.name == name_default
        assert product_name_min.name == name_min
        assert product_name_max.name == name_max

    def test_name_non_str_type(self):
        """
        Проверяет выбрасывание исключения при попытке передачи некорректного типа данных для наименования продукта.
        """
        name = 322
        with pytest.raises(ProductTypeError):
            ProductName(name=name)

    def test_name_length_less_than_minimum(self):
        """
        Проверяет выбрасывание исключения при попытке передачи наименования продукта длиной меньше минимальной.
        """
        name = 'В'*2
        with pytest.raises(MinLengthProductNameError):
            ProductName(name=name)

    def test_name_length_greater_than_maximum(self):
        """
        Проверяет выбрасывание исключения при попытке передачи наименования продукта длиной больше максимальной.
        """
        name = 'В'*101
        with pytest.raises(MaxLengthProductNameError):
            ProductName(name=name)

    def test_productnames_equality(self):
        """
        Проверяет равенство одинаковых наименований продуктов.
        """
        name = 'Велосипед'
        product_name1 = ProductName(name=name)
        product_name2 = ProductName(name=name)

        assert product_name1 == product_name2

    def test_productnames_inequality(self):
        """
        Проверяет неравенство разных наименований продуктов.
        """
        product_name1 = ProductName(name='Велосипед')
        product_name2 = ProductName(name='Самокат')

        assert product_name1 != product_name2
