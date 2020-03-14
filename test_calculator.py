from unittest import TestCase
from calculator import Calculator
from time import sleep


class TestCalculator(TestCase):
    def test_add(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(3, 4), 7)

    def test_multiply(self):
        sleep(0.1)
        self.fail()



