""" Import Calculation Parent Class Constructor """

from calculator.cal_calculation.calculation import Calculation

# pylint: disable=too-few-public-methods


class Multiplication(Calculation):
    """ Performs multiply between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ multiplies and return the values"""
        multiplication_of_values = 1
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return multiplication_of_values
