"""
Юнит-тесты модели DAO ProductDao.
"""
from uuid import UUID

from decimal import Decimal

from app.core.product.domain.product_entity import Product
from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_category import ProductCategory
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID
from app.core.product.infrastructure.models.product_dao import ProductDao


class TestProductDao:
    """
    Юнит-тесты для модели DAO :class:`ProductDao`
    """

    def test_to_dict_should_create_dict_with_columns_name_and_values(self):
        """
        Проверяет создание словаря из DAO продукта, где ключ - название столбца, а значение - значение в столбце.
        """
        product_dao = ProductDao(id=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'),
                                 name='Велосипед',
                                 category=ProductCategory.SPORT,
                                 price=19999.99,
                                 available_count=3)

        assert product_dao.to_dict() == {'id': UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'),
                                         'name': 'Велосипед',
                                         'category': ProductCategory.SPORT,
                                         'price': 19999.99,
                                         'available_count': 3}

    def test_to_entity_should_create_entity_instance(self):
        """
        Проверяет создание сущности продукта из DAO продукта.
        """
        product_dao = ProductDao(id=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'),
                                 name='Велосипед',
                                 category=ProductCategory.SPORT,
                                 price=19999.99,
                                 available_count=3)
        product = product_dao.to_entity()

        assert product.uuid == ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))
        assert product.name == ProductName('Велосипед')
        assert product.category == ProductCategory.SPORT
        assert product.price == Price(19999.99)
        assert product.available_count == ProductCount(3)

    def test_from_entity_should_create_dao_instance(self):
        """
        Проверяет создание DAO продукта из сущности продукта.
        """
        product = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                          name=ProductName('Велосипед'),
                          category=ProductCategory.SPORT,
                          price=Price(19999.99),
                          available_count=ProductCount(3))
        product_dao = ProductDao.from_entity(product)

        assert product_dao.id == UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')
        assert product_dao.name == 'Велосипед'
        assert product_dao.category == ProductCategory.SPORT
        assert product_dao.price == Decimal('19999.99')
        assert product_dao.available_count == 3
