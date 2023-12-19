def equilateral(sides):
    if sides[0]>0 and sides[1]>0 and sides[2]>0:
        return bool(sides[0]==sides[1]==sides[2])
    else:
        return False