"""Functions for tracking poker hands and assorted card tasks.
 
Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
def get_rounds(number):
    """Create a list containing the current and next two round numbers.
 
    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number+1, number+2]
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.
 
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.
 
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds