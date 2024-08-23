"""
Юнит-тесты сервиса продуктов ProductService.
"""
from decimal import Decimal
from uuid import UUID

import pytest

from app.core.product.application.exceptions import ProductNotFoundException
from app.core.product.application.schemas.product_create_schema import ProductCreateSchema
from app.core.product.application.schemas.product_read_schema import ProductReadSchema
from app.core.product.application.schemas.product_update_schema import ProductUpdateSchema
from app.core.product.application.services.product_service import ProductService
from app.core.product.domain.product_entity import Product
from app.core.product.domain.utils.product_filter_params import ProductFilterParams
from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_category import ProductCategory
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID
from app.core.shared_kernel.db.exceptions import EntityNotFoundException
from tests.unit.product.application.conftest import get_mock_product_repository


class TestProductService:
    """
    Юнит-тесты для сервиса продуктов :class:`ProductService`
    """

    async def test_add_product_should_return_product(self):
        """
        Проверяет добавление продукта через сервис и возвращение добавленного продукта.
        """
        mock_product_repository = get_mock_product_repository()

        product_to_add = ProductCreateSchema(name='Велосипед',
                                             category=ProductCategory.SPORT,
                                             price=19999.99,
                                             available_count=3)
        product_service = ProductService(mock_product_repository)
        added_product = await product_service.add_product(product_to_add)

        assert isinstance(added_product, ProductReadSchema)
        assert isinstance(added_product.uuid, UUID)
        assert added_product.name == 'Велосипед'
        assert added_product.category == ProductCategory.SPORT
        assert added_product.price == Decimal('19999.99')
        assert added_product.available_count == 3

    async def test_get_product_by_id_should_return_product(self):
        """
        Проверяет получение продукта по идентификатору.
        """
        mock_product = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                               name=ProductName('Велосипед'),
                               category=ProductCategory.SPORT,
                               price=Price(19999.99),
                               available_count=ProductCount(3))
        mock_product_repository = get_mock_product_repository()
        mock_product_repository.get_by_id.return_value = mock_product

        product_service = ProductService(mock_product_repository)
        product = await product_service.get_product_by_id(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))

        assert isinstance(product, ProductReadSchema)
        assert product.uuid == UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')
        assert product.name == 'Велосипед'
        assert product.category == ProductCategory.SPORT
        assert product.price == Decimal('19999.99')
        assert product.available_count == 3

    async def test_get_all_products_should_return_list_of_products(self):
        """
        Проверяет получение списка всех продуктов.
        """
        mock_products = [
            Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                    name=ProductName('Велосипед'),
                    category=ProductCategory.SPORT,
                    price=Price(19999.99),
                    available_count=ProductCount(3)),
            Product(uuid=ProductUUID(UUID('262f8c19-27c0-4e3c-b096-f6147ac052a3')),
                    name=ProductName('Самокат'),
                    category=ProductCategory.SPORT,
                    price=Price(9899.99),
                    available_count=ProductCount(10)),
            Product(uuid=ProductUUID(UUID('9bae1680-bc4f-40bf-9949-9639e08af3bd')),
                    name=ProductName('Хорошая книга'),
                    category=ProductCategory.OTHER,
                    price=Price(150.00),
                    available_count=ProductCount(1000)),
        ]
        mock_product_repository = get_mock_product_repository()
        mock_product_repository.get_all.return_value = mock_products

        product_service = ProductService(mock_product_repository)

        for page in range(1, 3):
            product_filter_params = ProductFilterParams(page=page, per_page=2)
            products = await product_service.get_all_products(product_filter_params=product_filter_params)

            received_mock_products = mock_products[(page-1)*2:page*2]

            assert isinstance(products, list)
            for product, mock_product in zip(products, received_mock_products):
                assert isinstance(product, ProductReadSchema)
                assert product.uuid == mock_product.uuid.uuid
                assert product.name == mock_product.name.name
                assert product.category == mock_product.category
                assert product.price == mock_product.price.price
                assert product.available_count == mock_product.available_count.count

    async def test_update_product_should_return_product(self):
        """
        Проверяет обновление продукта через сервис и возвращение обновлённого продукта.
        """
        mock_product = Product(uuid=ProductUUID(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')),
                               name=ProductName('Велосипед'),
                               category=ProductCategory.SPORT,
                               price=Price(19999.99),
                               available_count=ProductCount(3)),
        mock_product_repository = get_mock_product_repository()
        mock_product_repository.update.return_value = mock_product

        product_service = ProductService(mock_product_repository)
        product_to_update_uuid = UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')
        product_to_update = ProductUpdateSchema(name='Велосипед',
                                                category=ProductCategory.SPORT,
                                                price=19999.99,
                                                available_count=3)
        updated_product = await product_service.update_product(product_to_update_uuid, product_to_update)

        assert isinstance(updated_product, ProductReadSchema)
        assert updated_product.uuid == UUID('777a3f52-ce9a-4758-a4d4-881221f94f63')
        assert updated_product.name == 'Велосипед'
        assert updated_product.category == ProductCategory.SPORT
        assert updated_product.price == Decimal('19999.99')
        assert updated_product.available_count == 3

    async def test_delete_not_exists_product_should_raise_exception(self):
        """
        Проверяет удаление продукта через сервис по несуществующему идентификатору и возвращение исключения.
        """
        mock_product_repository = get_mock_product_repository()
        mock_product_repository.delete_by_id.side_effect = EntityNotFoundException

        product_service = ProductService(mock_product_repository)
        with pytest.raises(ProductNotFoundException):
            await product_service.delete_product_by_id(UUID('777a3f52-ce9a-4758-a4d4-881221f94f63'))
