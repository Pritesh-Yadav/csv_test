""" import all the methods from calc_methods"""


class History:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Clear the history array """
        History.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        History.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return History.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Gets last calculation from history array """
        return History.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Gets number of calculations from history array """
        return len(History.history)
