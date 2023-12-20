def equilateral(sides):
    if sides[0]>0 and sides[1]>0 and sides[2]>0:
        return bool(sides[0]==sides[1]==sides[2])
    else:
        return False

def isosceles(sides):
    a = sides[0]+sides[1]
    b = sides[1]+sides[2]
    c = sides[2]+sides[0]
    if a>=sides[2] and b>=sides[0] and c>=sides[1]:
        return bool(sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2])
    else:
        return False

