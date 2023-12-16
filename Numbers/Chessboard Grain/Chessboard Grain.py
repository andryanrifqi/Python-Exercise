def square(number):
    """Handle and throw ValueError if input is not as specified"""
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")

    """Count the number of grains on designated tiles as determined by input number"""    
    grains = pow(2,number-1)
    return grains

def total():
    """Count the total number of grains on every tiles on the board"""
    return 2**64-1