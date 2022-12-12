from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:
    def __init__(self, request: Request, storages: dict[str, AbstractStorage]):
        self.__request = request
        self.__from = storages[self.__request.from_]
        self.__to = storages[self.__request.to_]

    def move(self):
        self.__from.remove(name=self.__request.name_product, quantity=self.__request.quantity)

        print(f"Курьер забрал {self.__request.quantity} {self.__request.name_product} из {self.__request.from_}")
        print(f"Курьер везет {self.__request.quantity} {self.__request.name_product}")

        self.__to.add(name=self.__request.name_product, quantity=self.__request.quantity)
        print(f"Курьер доставил {self.__request.quantity} {self.__request.name_product} в {self.__request.to_}")

    def cancel(self):
        self.__from.add(name=self.__request.name_product, quantity=self.__request.quantity)
        print(f"Курьер вернул {self.__request.quantity} {self.__request.name_product} в {self.__request.from_}")



