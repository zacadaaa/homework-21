from entity.abstract_storage import AbstractStorage
from entity.exceptions import NotEnoughSpaceError, NotEnoughProductError, UnknownProductError


class BaseStorage(AbstractStorage):
    def __init__(self, items: dict[str, int], capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, quantity):

        if self.get_free_space() < quantity:
            raise NotEnoughSpaceError

        if name not in self._items:
            self._items[name] = quantity
        else:
            self._items[name] += quantity

    def remove(self, name, quantity):

        if name in self._items:

            if self._items[name] < quantity:
                raise NotEnoughProductError
            else:
                self._items[name] -= quantity

            if self._items[name] == 0:
                self._items.pop(name)

        else:
            raise UnknownProductError

    def get_free_space(self):

        for quantity in self._items.values():
            self._capacity -= quantity

        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
