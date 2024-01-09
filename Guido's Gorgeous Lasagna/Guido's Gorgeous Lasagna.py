EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param input: int - the number of layers in the lasagna.
    :return: elapsed_bake_time - total time elapsed (in minutes) preparing and cooking.
    """
    cooking_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return cooking_time_remaining
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate the elapsed cooking time.

    :param input: int - the number of layers in the lasagna.
    :return: elapsed_bake_time - total time elapsed (in minutes) preparing and cooking.
    """
    preparation_time = number_of_layers * LAYER_PREPARATION_TIME
    return preparation_time
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    total_cooking_time = (number_of_layers * LAYER_PREPARATION_TIME) + elapsed_bake_time
    return total_cooking_time

    
