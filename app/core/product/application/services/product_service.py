"""
Сервис для работы с продуктами ProductService.
"""

from uuid import uuid4, UUID

from app.core.product.application.exceptions import ProductNotFoundException, ProductExistsException
from app.core.product.application.schemas.product_create_schema import ProductCreateSchema
from app.core.product.application.schemas.product_read_schema import ProductReadSchema
from app.core.product.application.schemas.product_update_schema import ProductUpdateSchema
from app.core.product.domain.product_entity import Product
from app.core.product.domain.product_repository import ProductRepository
from app.core.product.domain.utils.product_filter_params import ProductFilterParams
from app.core.product.domain.value_objects.price import Price
from app.core.product.domain.value_objects.product_count import ProductCount
from app.core.product.domain.value_objects.product_name import ProductName
from app.core.product.domain.value_objects.product_uuid import ProductUUID
from app.core.shared_kernel.db.exceptions import EntityExistsException, EntityNotFoundException


class ProductService:
    """
    Сервис для работы с продуктами.

    :ivar product_repository: Репозиторий продуктов.
    """

    def __init__(self, product_repository: ProductRepository):
        """
        Конструктор ProductService.

        :param product_repository: Репозиторий продуктов.
        """
        self.product_repository = product_repository

    async def add_product(self, data: ProductCreateSchema) -> ProductReadSchema:
        """
        Добавляет новый продукт.

        :param data: Данные для создания продукта.
        :return: Информация созданного продукта.
        :raise ProductExistsException: Добавление продукта, который уже существует.
        """
        
        product = Product(
            uuid=ProductUUID(uuid4()),
            name=ProductName(data.name),
            category=data.category,
            price=Price(data.price),
            available_count=ProductCount(data.available_count)
        )

        try:
            await self.product_repository.add(product)
        except EntityExistsException as e:
            raise ProductExistsException from e

        return ProductReadSchema.from_entity(product)

    async def get_product_by_id(self, id_: UUID) -> ProductReadSchema:
        """
        Получает информацию о продукте по его идентификатору.

        :param id_: Уникальный идентификатор продукта.
        :return: Информация о продукте.
        :raise ProductNotFoundException: Продукт не был найден.
        """
        product = await self.product_repository.get_by_id(id_)
        if not product:
            raise ProductNotFoundException

        return ProductReadSchema.from_entity(product)

    async def get_all_products(self, product_filter_params: ProductFilterParams) -> list[ProductReadSchema]:
        """
        Получает информацию о всех продуктах по фильтру.

        :return: Список с информацией о продуктах.
        """

        products = await self.product_repository.get_by_filter(product_filter_params=product_filter_params)
        return [ProductReadSchema.from_entity(product) for product in products]

    async def update_product(self, data: ProductUpdateSchema) -> ProductReadSchema:
        """
        Обновляет продукт.

        :param data: Данные для обновления продукта.
        :return: Информация обновленного продукта.
        :raise ProductNotFoundException: Обновление продукта, который не найден.
        :raise ProductExistsException: Добавление продукта, который уже существует.
        """
        new_product = Product(
            uuid=ProductUUID(data.uuid),
            name=ProductName(data.name),
            category=data.category,
            price=Price(data.price),
            available_count=ProductCount(data.available_count)
        )
        try:
            await self.product_repository.update(new_product)
        except EntityNotFoundException as e:
            raise ProductNotFoundException from e
        except EntityExistsException as e:
            raise ProductExistsException from e

        return ProductReadSchema.from_entity(new_product)

    async def delete_product_by_id(self, id_: UUID) -> None:
        """
        Удаляет продукт по его идентификатору.

        :param id_: Уникальный идентификатор продукта.
        """

        try:
            await self.product_repository.delete_by_id(id_)
        except EntityNotFoundException as e:
            raise ProductNotFoundException from e
