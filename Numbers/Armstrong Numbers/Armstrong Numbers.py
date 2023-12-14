def is_armstrong_number(number):
    digits = [int(_) for _ in str(number)]
    new_number = 0
    
    for digit in digits:
        new_number += pow(digit,len(digits))
        
    return bool(new_number == number)
