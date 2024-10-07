import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calculator.division(self, 20, 4) == 5

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 12, 7) != 7

    def test_adding_success(self):
        assert self.calculator.adding(self,3, 5) == 8

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
