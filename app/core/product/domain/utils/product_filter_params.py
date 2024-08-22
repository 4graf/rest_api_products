"""
Параметры для фильтрации продуктов ProductFilterParams.
"""

from pydantic import BaseModel, Field


class ProductFilterParams(BaseModel):
    """
    Параметры для фильтрации продуктов.

    :ivar page: Номер страницы с продуктами, начиная с 0.
    :ivar per_page: Количество продуктов на странице.
    """

    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
