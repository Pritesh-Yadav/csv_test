""" import all the methods from calc_methods"""
import logging
import sys
from calculator.calc.addition import Addition
from calculator.calc.subtraction import Subtraction
from calculator.calc.multiplication import Multiplication
from calculator.calc.division import Division
from calculator.calchistory.calc_history import History
from csv_handling.read import CSVRead

sys.tracebacklimit = 0
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('log/sample.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []
    data = []
    path = ''

    def __init__(self, path):
        self.data = CSVRead.read_data(path)
        self.path = path
        self.move_path = path.replace("input", "done")

    def get_data(self):
        """ Splits the data and returns all columns """
        csv_data = self.data
        num1 = csv_data['input_1'].values
        num2 = csv_data['input_2'].values
        add = [round(i, 3) for i in csv_data['add'].values]
        sub = [round(i, 3) for i in csv_data['sub'].values]
        multi = [round(i, 3) for i in csv_data['multi'].values]
        div = [round(i, 3) for i in csv_data['div'].values]

        return num1, num2, add, sub, multi, div

    @staticmethod
    def add_nums(*args):
        """ Adds given list of numbers and appends the result to history """
        addition = Addition(args).getresult()
        logger.debug('Add: %f + %f = %f', args[0], args[1], addition)
        History.add_calculation_history(addition)
        return History.get_last_calculation()

    @staticmethod
    def subtract_nums(*args):
        """ Subtracts given list of numbers and appends the result to history """
        subtraction = Subtraction(args).getresult()
        logger.debug('Subtract: %f - %f = %f', args[0], args[1], subtraction)
        History.add_calculation_history(subtraction)
        return History.get_last_calculation()

    @staticmethod
    def multiply_nums(*args):
        """ Multiplies given list of numbers and appends the result to history """
        multiplication = Multiplication(args).getresult()
        logger.debug('Multiply: %f * %f = %f', args[0], args[1], multiplication)
        History.add_calculation_history(multiplication)
        return History.get_last_calculation()

    @staticmethod
    def divide_nums(*args):
        """ Divides given list of numbers and appends the result to history """
        try:
            division = Division(args).getresult()
            History.add_calculation_history(division)
        except ZeroDivisionError as err:
            logger.exception(err)
            return 0.0
        else:
            logger.debug('Divide: %f / %f = %f', args[0], args[1], division)
            return History.get_last_calculation()
