import unittest
import python_programming.calculator as calculator


class TestCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc(10,20)
        self.assertEqual(result,30)

    def test_add_functionality_with_negative(self):
        result = calculator.calc(-10, -20)
        self.assertEqual(result, -30)

    def test_add_functionality_diff(self):
        result = calculator.calc(-10, 20)
        self.assertEqual(result, 10)