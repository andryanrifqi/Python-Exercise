def is_armstrong_number(number):
    digits = [int(_) for _ in str(number)]
    pwr = len(digits)
    new_number = 0
    
    for digit in digits:
        new_number += pow(digit,pwr)
        
    return bool(new_number == number)