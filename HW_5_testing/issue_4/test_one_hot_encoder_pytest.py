import pytest
from one_hot_encoder import fit_transform


def test_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_dimensions():
    fruits = ['apple', 'orange', 'apple', 'apple', 'orange', 'pineapple']
    result_list = fit_transform(fruits)
    result_list_example = result_list[0]
    result_binary_list = result_list_example[1]
    dimension = len(result_binary_list)
    assert dimension == len(set(fruits))


def test_return_type():
    values = [1, 2, 3, 1, 1]
    assert isinstance(fit_transform(values), list)


def test_empty_entry():
    with pytest.raises(TypeError):
        fit_transform()
