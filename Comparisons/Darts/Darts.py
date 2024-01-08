import math

def score(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    
    return (distance <= 1) * 5 + (distance <= 5) * 4 + (distance <= 10) * 1