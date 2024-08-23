"""
Юнит-тесты объекта значения Price.
"""

import pytest
from decimal import Decimal

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.exceptions.product_price_exceptions import ProductPriceLessThanZeroError, \
    MaxValueProductPriceError
from app.core.product.domain.value_objects.price import Price
from tests.utils import idfn


class TestPrice:
    """
    Юнит-тесты для объекта значения :class:`Price`
    """

    @pytest.mark.parametrize('param',
                             (
                                     0,
                                     0.01,
                                     1_000_000_000,
                                     999_999_999.99,
                                     Decimal('12.23'),
                                     123,
                                     123.12,
                                     '12.3',
                             ),
                             ids=idfn)
    def test_create_valueobject_price(self, param):
        """
        Проверяет корректное создание объекта значения цены.
        """

        price = Price(price=param)

        assert price.price == Decimal(str(param))

    @pytest.mark.parametrize('param, expected',
                             (
                                     (100.124, Decimal('100.13')),
                                     (3.991, Decimal('4')),
                                     (5.120, Decimal('5.12'))
                             ),
                             ids=idfn)
    def test_price_two_decimal_rounding(self, param, expected):
        price = Price(param)

        assert price.price == expected

    @pytest.mark.parametrize('param',
                             (
                                 'a',
                                 '1a',
                                 [123],
                                 {1: 2}
                             ),
                             ids=idfn)
    def test_price_non_correct_type(self, param):
        """
        Проверяет выбрасывание исключения при попытке передачи некорректного типа данных для цены.
        """
        with pytest.raises(ProductTypeError):
            Price(price=param)

    def test_price_less_than_zero(self):
        """
        Проверяет выбрасывание исключения при попытке передачи цены меньше 0.
        """
        price = -0.01
        with pytest.raises(ProductPriceLessThanZeroError):
            Price(price=price)

    def test_price_greater_than_maximum(self):
        """
        Проверяет выбрасывание исключения при попытке передачи цены больше максимальной.
        """
        price = 1_000_000_000.01
        with pytest.raises(MaxValueProductPriceError):
            Price(price=price)

    def test_prices_equality(self):
        """
        Проверяет равенство одинаковых цен.
        """
        price = 123.123
        price1 = Price(price=price)
        price2 = Price(price=price)

        assert price1 == price2

    def test_prices_inequality(self):
        """
        Проверяет неравенство разных цен.
        """
        price1 = Price(123.123)
        price2 = Price(123.133)

        assert price1 != price2
