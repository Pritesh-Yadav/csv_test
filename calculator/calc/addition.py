""" Import Calculation Parent Class Constructor """
from calculator.calc.calculation import Calculation
# pylint: disable=too-few-public-methods


class Addition(Calculation):
    """ Performs addition between two values  """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = sum_of_values + value
        return sum_of_values
