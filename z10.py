import math
a = 1
b = 8
c = 6
#delta
D = b*b-4*a*c
if D > 0:
    math.sqrt(D)
    x1 = (-b - D ) / (a*2)
    x2 = (-b + D ) / (a*2)
    print("Miejsca zerowe: " +  str(round(x1)) + ' ' +  str(round(x2)))
elif D == 0:
    x1 = -b / (a * 2)
    print("Miejsce zerowe: " + str(round(x1)))
else:
    print("Nie ma miejsc zerowych")