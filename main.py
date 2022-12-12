from entity.shop import Shop
from entity.store import Storage
from entity.request import Request
from entity.courier import Courier
from entity.exceptions import BaseError


shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 2,
    }
)

store = Storage(
    items={
        'печенька': 10,
        'ноутбук': 20,

    }
)

storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    while True:

        for storage in storages:

            print(f"В {storage} хранится: {storages[storage].get_items()}")

        user_input = input(
            "Введите запрос в формате 'Доставить 3 печенька из склад в магазин'\n"
            "Введите 'stop' или 'стоп' чтобы продолжить\n"
        )

        if user_input in ["stop", 'стоп']:
            break

        try:
            request = Request(request=user_input, storages=storages)

        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()

        except BaseError as e:
            print(e.message)
            courier.cancel()


if __name__ == '__main__':
    main()