"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate Preparationtime in minutes

    :param number_of_layers: int - layers to add to lasagna.
    :return: int - preparation time (in minutes) 

     function that takes the number_of_layers you want to add to the lasagna as an         argument and returns how many minutes you would spend making them. Assume each        layer takes 2 minutes to prepare. Based on PREPARATION_TIME
    """
    return PREPARATION_TIME * number_of_layers


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate Total Elapsed Time

    :param number_of_layers: int - layers to add to lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has spent                                           baking in the oven already
    :return: int - Total minutes you have been in the kitchen cooking 

     """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
