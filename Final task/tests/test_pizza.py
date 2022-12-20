from pizza import Hawaiian, Pepperoni, Margherita, PizzaSize


def test_diff_not_equal():
    assert Hawaiian() != Pepperoni()


def test_same_equal():
    assert Margherita() == Margherita()


def test_equal_diff_size():
    assert Margherita(PizzaSize.BIG) != Margherita()


def test_pizza_dict():
    expected = {'Margherita': 'tomato sauce, mozzarella, tomatoes'}
    assert Margherita().dict() == expected


