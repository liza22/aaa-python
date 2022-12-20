from enum import Enum


class PizzaSize(Enum):
    """Возможные размеры пиццы"""

    CLASSIC = "L"
    BIG = "XL"


class Pizza:
    """Базовый класс пиццы"""

    icon = ""
    ingredients: list[str] = []

    @classmethod
    def dict(cls) -> dict[str, str]:
        return {cls.__name__: ", ".join(cls.ingredients)}

    def __init__(self, size: PizzaSize = PizzaSize.CLASSIC):
        self.size = size

    def __eq__(self, other) -> bool:
        return (self.ingredients == other.ingredients
                and self.size is other.size)


class Margherita(Pizza):
    """Пицца Маргарита"""

    icon = "\U0001F9C0"
    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]


class Pepperoni(Pizza):
    """Пицца Пепперони"""

    icon = "\U0001F355"
    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]


class Hawaiian(Pizza):
    """Пицца Гавайская"""

    icon = "\U0001F34D"
    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
