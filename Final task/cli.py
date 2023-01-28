import click

import service
from pizza import Pizza, PizzaSize


def get_pizza_by_name(pizza_name: str, big: bool) -> Pizza:
    """
    Ищет класс пиццы с запрашиваемым названием.
    Возвращает экземпляр найденного класса, если такой есть.
    Иначе кидает исключение
    """
    for pizza in Pizza.__subclasses__():
        if pizza.__name__.lower() == pizza_name:
            return pizza(PizzaSize.BIG) if big else pizza()
    raise NameError


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Выводит меню"""
    for pizza in Pizza.__subclasses__():
        recipe = pizza.dict()
        ingredients = list(recipe.values())[0]
        print(f"- {pizza.__name__} {pizza.icon}: {ingredients}")


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--big", default=False, is_flag=True)
@click.argument("pizza_name", nargs=1)
def order(pizza_name: str, delivery: bool, big: bool):
    """Готовит и доставляет пиццу"""
    try:
        pizza = get_pizza_by_name(pizza_name, big)
        service.bake(pizza)
    except NameError:
        print(
            "Такой пиццы не существует. "
            "Вызовите команду menu для просмотра доступного меню."
        )
        return

    if delivery:
        service.delivery(pizza)
    else:
        service.pickup(pizza)


if __name__ == "__main__":
    cli()
