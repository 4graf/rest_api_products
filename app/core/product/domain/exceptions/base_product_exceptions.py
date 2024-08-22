"""
Базовые исключения для продуктов.
"""


class ProductException(Exception):
    """
    Базовое исключение для продуктов.
    """


class ProductValidationException(ProductException):
    """
    Базовое исключение для валидации продуктов.
    """


class ProductTypeError(ProductValidationException):
    """
    Исключение, возникающее при несоответствии типа данных.
    """
    def __init__(self, msg: str = 'Ошибка валидации', extra_msg_exception: str = None):
        """
        Конструктор ProductTypeError.

        :param msg: Сообщение исключения.
        :param extra_msg_exception: Дополнительное сообщение исключения.
        """
        if extra_msg_exception:
            msg = f'{msg}: {extra_msg_exception}'
        super().__init__(msg)
