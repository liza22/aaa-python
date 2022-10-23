import json

LESSON_STR = """{
    "title": "python",
    "price": 10,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
    }
}"""

CORGI_STR = """{
    "title": "Вельш-корги",
    "price": 1000,
    "category": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, \
        поселок санатория Тишково, 25"
    }
}"""


class ColorizeMixin:
    """Миксин для ИЗМЕНЕНИЯ цвета текста при выводе на консоль"""

    def __str__(self):
        return f'\033[{self.repr_color_code}m{self.title} | {self.price} ₽'


class DotAttribute:
    """
    Вспомогательный класс для разбора вложенных полей объявления.
    Преобразовывает JSON в python-объеĸты с доступом ĸ атрибутам через точку.
    """

    def __init__(self, obj: dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                self.__setattr__(key, DotAttribute(value))
            else:
                self.__setattr__(key, value)

    def __setattr__(self, key: str, value: (str, list, dict)):
        self.__dict__[key] = value


class Advert(ColorizeMixin, DotAttribute):
    """
    Реализует объект "объявление".
    Динамически создает атрибуты экземпляра класса из атрибутов JSON-объеĸта.
    Предоставляет доступ к атрибутам через точку.
    Атрибуты класса:
       repr_color_code - цвет текста при выводе в консоль
    """
    repr_color_code = 94

    def __init__(self, obj: dict):
        """
        Экземпляр объявления должен содржать неотрицательную цену.
        Если задана отрицательная цена - выкидывает исключение.
        Если цена не задана, она устанавливается в 0.
        """
        price = obj.get("price", 0)
        if price < 0:
            raise ValueError("price must be >= 0")
        self.price = price
        super().__init__(obj)

    def __repr__(self) -> str:
        """Вывод информации об объявлении"""
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    non_price_ad = Advert({"title": "python"})
    print(non_price_ad.price)

    try:
        neg_price_ad = Advert({"title": "python", "price": -100})
    except ValueError as e:
        print(f"Got exception: {e}")

    lesson = json.loads(LESSON_STR)
    lesson_ad = Advert(lesson)
    print(f"Адрес: {lesson_ad.location.address},"
          f"станции метро: {lesson_ad.location.metro_stations}")

    corgi = json.loads(CORGI_STR)
    corgi_ad = Advert(corgi)
    print(corgi_ad.category)

    print(corgi_ad)
