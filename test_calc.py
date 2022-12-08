import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_succes(self):
        assert self.calc.adding(1, 1) == 2

    # def test_adding_unsucces(self):
    #     assert self.calc.adding(1, 1) == 3

    def test_division_succes(self):
        assert self.calc.division(8, 2) == 4

    # def test_division_unsucces(self):
    #     assert self.calc.division(8, 2) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_multiply_succes(self):
        assert self.calc.multiply(2, 5) == 10

    # def test_multiply_unsucces(self):
    #     assert self.calc.multiply(2, 5) == 9

    def test_subtraction_succes(self):
        assert self.calc.subtraction(5, 2) == 3

    # def test_subtraction_unsucces(self):
    #     assert self.calc.subtraction(5, 4) == 11

    def teardown(self):
        print('Выполнение метода Teardown')
