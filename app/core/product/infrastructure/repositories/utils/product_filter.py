"""
ProductFilter фильтр для запросов продуктов.
"""

from sqlalchemy import Select

from app.core.product.domain.utils.product_filter_params import ProductFilterParams


class ProductFilter:
    """
    Фильтр для запросов продуктов.
    """

    @classmethod
    def filter_query(cls, query: Select, product_filter_params: ProductFilterParams) -> Select:
        """
        Добавляет фильтр к запросу.

        :param query: Select запрос на выбор продуктов.
        :param product_filter_params: Параметры фильтрации.
        :return: Select запрос с применёнными фильтрами.
        """

        offset = (product_filter_params.page - 1) * product_filter_params.per_page
        return query.offset(offset).limit(product_filter_params.per_page)
