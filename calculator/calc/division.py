""" Import Calculation Parent Class Constructor """

from calculator.cal.calculation import Calculation

# This is division method which inherits the calculation class constructor


class Division(Calculation):
    """ Performs division between two values """

    def getresult(self):
        """ divides and returns the values """
        division_of_values = self.values[0]
        for value in self.values[1:]:
            division_of_values = division_of_values / value
        return division_of_values
