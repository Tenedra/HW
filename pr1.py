import math


a, b, c = map(float, input().split())

if (2*(a+b)+5)<0 or 4*math.sin(c/2) == 0 or (a*b**2+18)<0:
    print("Error, enter other nambers")
else:
    print((a+math.sqrt(2*(a+b)+5))/(4*math.sin(c/2))+math.pow(a*b**2+18, 1/4)+math.pow(math.cos(c), a-b))
