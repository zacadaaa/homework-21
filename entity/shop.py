from entity.base_storage import BaseStorage
from entity.exceptions import TooManyUniqueProductError


class Shop(BaseStorage):
    def __init__(self, items: dict[str, int], capacity=20):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_unique_items_count() >= 5:
            raise TooManyUniqueProductError

        super().add(name, quantity)