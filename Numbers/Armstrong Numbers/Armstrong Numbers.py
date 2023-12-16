def is_armstrong_number(number):
    """Parse input numbers into list"""
    digits = [int(_) for _ in str(number)]
    new_number = 0
    
    """Loop for every number in the list, count every number to the power of the length of input number"""
    for digit in digits:
        new_number += pow(digit,len(digits))

    """Check and return the Armstrong Number result"""    
    return bool(new_number == number)
