"""
Перечисление категорий продуктов.
"""
from enum import Enum


# ToDo: в дальнейшем следовало бы вынести в отдельную сущность.
class ProductCategory(Enum):
    """
    Перечисление категорий продуктов.
    """
    FOOD = "FOOD"
    TECHNIQUE = "TECHNIC"
    SPORT = "SPORT"
    OTHER = "OTHER"
