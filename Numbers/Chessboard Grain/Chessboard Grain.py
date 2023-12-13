def square(number):
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
        
    grains = pow(2,number-1)
    return grains
def total():
    count = 1
    pwr=0
    
    while count <= 65:
        total_grain = pow(2,pwr)
        pwr+=1
        count+=1
    return total_grain-1