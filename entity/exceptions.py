class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class TooManyUniqueProductError(BaseError):
    message = 'Много уникальных товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'
