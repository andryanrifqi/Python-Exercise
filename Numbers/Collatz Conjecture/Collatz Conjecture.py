def steps(number):
    counter = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
        
    while number > 1 :
        if number % 2 == 0:
            number = number / 2
            
        else:
            number = number * 3 + 1
        counter += 1
    
    return counter