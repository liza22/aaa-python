import pytest

from cli import get_pizza_by_name, menu, order, cli
from pizza import Hawaiian, Pepperoni, Margherita, PizzaSize
from click.testing import CliRunner


def test_get_existing_pizza():
    pizza = get_pizza_by_name('margherita', False)
    assert pizza == Margherita()


def test_get_not_existing_pizza():
    with pytest.raises(NameError):
        get_pizza_by_name('margarita', False)


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert len(result.output.strip().split('\n')) == 3


def test_order_incorrect():
    runner = CliRunner()
    result = runner.invoke(order, ['margarita'])
    expected = (
            "Такой пиццы не существует. "
            "Вызовите команду menu для просмотра доступного меню."
    )
    assert result.output.strip() == expected


def test_order_big_flag():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--big'])
    assert 'XL' in result.output.strip()


def test_order_delivery_flag():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--delivery'])
    assert '\U0001F697 Доставили за' in result.output.strip()