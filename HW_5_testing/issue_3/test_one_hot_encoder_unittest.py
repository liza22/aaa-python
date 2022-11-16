from one_hot_encoder import fit_transform
import unittest


class TestEncoder(unittest.TestCase):
    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_dimensions(self):
        fruits = ['apple', 'orange', 'apple', 'apple', 'orange', 'pineapple']
        dimension = len(fit_transform(fruits)[0][1])
        self.assertTrue(dimension == len(set(fruits)))

    def test_return_type(self):
        values = [1, 2, 3, 1, 1]
        self.assertIsInstance(fit_transform(values), list)

    def test_empty_entry(self):
        with self.assertRaises(TypeError):
            fit_transform()
