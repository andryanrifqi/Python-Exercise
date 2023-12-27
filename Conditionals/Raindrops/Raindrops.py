def convert(number):
    factors = []
    for i in range(1, number+1):
        if number%i == 0:
           factors.append(i)
    output = ""
    if 3 in factors:
        output += "Pling"
    if 5 in factors:
        output += "Plang"
    if 7 in factors:
        output += "Plong"

    if len(output) != 0:
        return output
    else:
        return str(number)