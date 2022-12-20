from service import bake, delivery, pickup
from pizza import Margherita


def test_bake(capsys):
    bake(Margherita())
    captured = capsys.readouterr().out.split('\n')
    bake_output = captured[0]
    log_output = captured[1]
    assert bake_output == "Приготовлена Margherita размера L"
    assert log_output.startswith("bake -")


def test_delivery(capsys):
    delivery(Margherita())
    captured = capsys.readouterr().out.split('\n')
    delivery_output = captured[0]
    log_output = captured[1]
    assert delivery_output == "Доставка пиццы Margherita"
    assert log_output.startswith("\U0001F697 Доставили за")


def test_pickup(capsys):
    pickup(Margherita())
    captured = capsys.readouterr().out.split('\n')
    pickup_output = captured[0]
    log_output = captured[1]
    assert pickup_output == "Пицца Margherita готова к самовывозу"
    assert log_output.startswith("\U0001F3E0 Забрали за")

