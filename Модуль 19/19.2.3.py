import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_pass(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_pass(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_pass(self):
        assert self.calc.subtraction(self, 58, 32) == 26

    def test_adding_pass(self):
        assert self.calc.adding(self, 54, 46) == 100

