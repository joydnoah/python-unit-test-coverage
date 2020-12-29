from unittest import TestCase
from methods import some_method


class TestMethod(TestCase):
    def test_one(self):
        result = some_method.method_for_testing(1, 2)
        self.assertEqual(1, result)
        result = some_method.method_for_testing(2, 1)
        self.assertEqual(1, result)

    def test_two(self):
        result = some_method.method_for_testing2(1, 2)
        self.assertEqual(-1, result)
        result = some_method.method_for_testing2(2, 1)
        self.assertEqual(-1, result)