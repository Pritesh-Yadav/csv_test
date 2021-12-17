"""Importing Calculator Class from calculator > main.py for Testing"""
import pytest
from calculator.main import Calculator
from calculator.historycalculations.history_calculations import History

# pylint: disable=unused-argument,redefined-outer-name

num1, num2, add, sub, multi, div = Calculator('csv_handling/input/data.csv').get_data()
length = len(add)


# This is called a fixture and it runs each time you pass it to a test
@pytest.fixture
def clear_history():
    """ Clears history """
    History.clear_history()


def test_calculator_add(clear_history):
    """ To check if calculator addition result is correct """

    for i in range(length):
        assert Calculator.add_nums(num1[i], num2[i]) == add[i]
    assert History.get_calculation_count() == 7
    assert History.get_last_calculation_added() == add[-1]
    assert History.get_first_calculation_history() == add[0]


def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    for i in range(length):
        assert Calculator.subtract_nums(num1[i], num2[i]) == sub[i]


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    for i in range(length):
        assert Calculator.multiply_nums(num1[i], num2[i]) == multi[i]


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    for i in range(length):
        assert Calculator.divide_nums(num1[i], num2[i]) == div[i]
