"""
Юнит-тесты объекта значения ProductUUID.
"""

from uuid import UUID

import pytest

from app.core.product.domain.exceptions.base_product_exceptions import ProductTypeError
from app.core.product.domain.value_objects.product_uuid import ProductUUID


class TestProductUUID:
    """
    Юнит-тесты для объекта значения :class:`ProductUUID`
    """

    def test_create_valueobject_productuuid(self):
        """
        Проверяет корректное создание объекта значения идентификатора продукта.
        """
        product_uuid = ProductUUID(uuid=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))

        assert product_uuid.uuid == UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')

    def test_uuid_non_uuid_type(self):
        """
        Проверяет выбрасывание исключения при попытке передачи некорректного типа данных для идентификатора продукта.
        """
        uuid = '777a'
        with pytest.raises(ProductTypeError):
            ProductUUID(uuid=uuid)

    def test_productuuids_equality(self):
        """
        Проверяет равенство одинаковых идентификаторов продуктов.
        """
        product_uuid1 = ProductUUID(uuid=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))
        product_uuid2 = ProductUUID(uuid=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))

        assert product_uuid1 == product_uuid2

    def test_productuuids_inequality(self):
        """
        Проверяет неравенство разных идентификаторов продуктов.
        """
        product_uuid1 = ProductUUID(uuid=UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))
        product_uuid2 = ProductUUID(uuid=UUID('262f8c19-27c0-4e3c-b096-f6147ac052a3'))

        assert product_uuid1 != product_uuid2
