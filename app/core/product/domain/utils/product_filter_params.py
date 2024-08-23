"""
Параметры для фильтрации продуктов ProductFilterParams.
"""
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field

from app.core.product.domain.value_objects.product_category import ProductCategory

class ProductOrderBy(Enum):
    """
    Перечисление для определения порядка сортировки продукта.
    """

    NAME = 'NAME'
    PRICE = 'PRICE'
    COUNT = 'COUNT'

class ProductOrderMode(Enum):
    """
    Перечисление для определения направления сортировки продукта (ascending - по возрастанию, descending - по убыванию).
    """

    ASC = 'ASC'
    DESC = 'DESC'

class ProductFilterParams(BaseModel):
    """
    Параметры для фильтрации продуктов.

    :ivar page: Номер страницы с продуктами.
    :ivar per_page: Количество продуктов на странице.
    """

    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
    category: ProductCategory | None = None
    price_from: Decimal | None = None
    price_to: Decimal | None = None
    show_only_available: bool | None = None
    order_by: ProductOrderBy = ProductOrderBy.PRICE
    order_mode: ProductOrderMode = ProductOrderMode.ASC
