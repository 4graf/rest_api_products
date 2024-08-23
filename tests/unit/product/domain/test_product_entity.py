"""
Юнит-тесты сущности Product.
"""

from uuid import UUID

from app.core.product.domain.product_entity import Product
from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_category import ProductCategory
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID


class TestProduct:
    """
    Юнит-тесты для сущности :class:`Product`
    """

    def test_create_entity_product(self):
        """
        Проверяет корректное создание сущности продукта.
        """
        product = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                          name=ProductName('Велосипед'),
                          category=ProductCategory.SPORT,
                          price=Price(19999.99),
                          available_count=ProductCount(3))

        assert product.uuid == ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))
        assert product.name == ProductName('Велосипед')
        assert product.category == ProductCategory.SPORT
        assert product.price == Price(19999.99)
        assert product.available_count == ProductCount(3)

    def test_product_identified_by_id(self):
        """
        Проверяет равенство продуктов по их идентификаторам.
        """
        product1 = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                           name=ProductName('Велосипед'),
                           category=ProductCategory.SPORT,
                           price=Price(19_999.99),
                           available_count=ProductCount(3))
        product2 = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                           name=ProductName('Велосипед спортивный'),
                           category=ProductCategory.SPORT,
                           price=Price(19_999.99),
                           available_count=ProductCount(3))
        product3 = Product(uuid=ProductUUID(UUID('262f8c19-27c0-4e3c-b096-f6147ac052a3')),
                           name=ProductName('Велосипед'),
                           category=ProductCategory.SPORT,
                           price=Price(19_999.99),
                           available_count=ProductCount(3))

        assert product1 == product2
        assert product1 != product3
