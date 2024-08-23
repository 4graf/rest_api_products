"""
Юнит-тесты объекта значения ProductCount.
"""

import pytest
from decimal import Decimal

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_count_exceptions import ProductCountLessThanZeroError, \
    MaxValueProductCountError
from app.core.product.domain.value_objects.product_count import ProductCount
from tests.utils import idfn


class TestProductCount:
    """
    Юнит-тесты для объекта значения :class:`ProductCount`
    """

    @pytest.mark.parametrize('param',
                             (
                                     0,
                                     1,
                                     1_000_000_000,
                                     999_999_999,
                                     150
                             ),
                             ids=idfn)
    def test_create_valueobject_productcount(self, param):
        """
        Проверяет корректное создание объекта значения количества продукта.
        """

        product_count = ProductCount(count=param)

        assert product_count.count == Decimal(str(param))

    @pytest.mark.parametrize('count',
                             (
                                 1.1,
                                 '1',
                                 'a',
                                 [1],
                                 {1: 2}
                             ),
                             ids=idfn)
    def test_productcount_non_correct_type(self, count):
        """
        Проверяет выбрасывание исключения при попытке передачи некорректного типа данных для количества продукта.
        """
        with pytest.raises(ProductTypeError):
            ProductCount(count=count)

    def test_productcount_less_than_zero(self):
        """
        Проверяет выбрасывание исключения при попытке передачи количества продукта меньше 0.
        """
        product_count = -1
        with pytest.raises(ProductCountLessThanZeroError):
            ProductCount(count=product_count)

    def test_productcount_greater_than_maximum(self):
        """
        Проверяет выбрасывание исключения при попытке передачи количества продуктов больше максимального.
        """
        count = 1_000_000_001
        with pytest.raises(MaxValueProductCountError):
            ProductCount(count=count)

    def test_productcounts_equality(self):
        """
        Проверяет равенство одинакового количества продукта.
        """
        product_count = 12
        product_count1 = ProductCount(count=product_count)
        product_count2 = ProductCount(count=product_count)

        assert product_count1 == product_count2

    def test_productcounts_inequality(self):
        """
        Проверяет неравенство разного количества продукта.
        """
        product_count1 = ProductCount(123)
        product_count2 = ProductCount(124)

        assert product_count1 != product_count2
