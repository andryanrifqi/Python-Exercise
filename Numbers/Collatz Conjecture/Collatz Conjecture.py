def steps(number):
    i=0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number>=2:
            if number%2 == 0:
                number=number/2
                i+=1
            else:
                number=number*3+1
                i+=1
    
    return i