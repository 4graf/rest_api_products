from unittest.mock import MagicMock

from app.core.product.domain.product_repository import ProductRepository


def get_mock_product_repository():
    """
    Создаёт заглушку репозитория для продуктов.
    """
    return MagicMock(spec=ProductRepository)
