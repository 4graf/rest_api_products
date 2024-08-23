"""
ProductFilter фильтр для запросов продуктов.
"""

from sqlalchemy import Select, and_, desc, case, asc, nulls_last

from app.core.product.domain.utils.product_filter_params import ProductFilterParams, ProductOrderBy, ProductOrderMode
from app.core.product.infrastructure.models.product_dao import ProductDao


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

        conditions = []

        if product_filter_params.category:
            conditions.append(ProductDao.category == product_filter_params.category.value)
        if product_filter_params.price_from:
            conditions.append(ProductDao.price >= product_filter_params.price_from)
        if product_filter_params.price_to:
            conditions.append(ProductDao.price <= product_filter_params.price_to)
        if product_filter_params.show_only_available:
            conditions.append(ProductDao.available_count > 0)

        query = query.where(and_(*conditions))

        order_mode = asc if product_filter_params.order_mode == ProductOrderMode.ASC else desc
        match product_filter_params.order_by:
            case ProductOrderBy.PRICE:
                sort = order_mode(ProductDao.price)
            case ProductOrderBy.NAME:
                sort = order_mode(ProductDao.name)
            case ProductOrderBy.COUNT:
                sort = order_mode(ProductDao.available_count)
            case _:
                sort = None

        query = query.order_by(case((ProductDao.available_count == 0, 1), else_=0))
        query = query.order_by(sort)

        offset = (product_filter_params.page - 1) * product_filter_params.per_page
        query = query.offset(offset).limit(product_filter_params.per_page)
        return query
