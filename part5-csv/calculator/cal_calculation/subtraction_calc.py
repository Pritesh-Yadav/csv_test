""" Import Calculation Parent Class Constructor """

from calculator.cal_calculation.calculation import Calculation

# pylint: disable=too-few-public-methods


class Subtraction(Calculation):
    """ Performs subtraction between two values coming from Parent Class  """

    def getresult(self):
        """ performs subtraction and returns the values """
        subtraction_of_values = self.values[0]
        for value in self.values[1:]:
            subtraction_of_values = subtraction_of_values - value
        return subtraction_of_values
