from entity.abstract_storage import AbstractStorage
from entity.exceptions import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request, storages: dict[str, AbstractStorage]):
        split_req = request.lower().split(' ')

        if len(split_req) != 7 or not split_req[1].isdigit():
            raise InvalidRequestError

        else:
            self.quantity = int(split_req[1])
            self.name_product = split_req[2]
            self.from_ = split_req[4]
            self.to_ = split_req[6]

        if self.from_ not in storages or self.to_ not in storages:
            raise UnknownStorageError
