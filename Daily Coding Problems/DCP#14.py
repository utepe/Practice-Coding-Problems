'''
The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.
'''
from random import randint, random
def estimatePI(totalPoints):
    radius = 0.5    #0.5 radius (circle enclosed by a 1*1 square)
    rSquare = radius**2
    innerCount = 0
    for _ in range(totalPoints):
        x = random() * radius
        y = random() * radius
        if (x**2 + y**2) <= rSquare:
            innerCount += 1
    return 4*innerCount/totalPoints

print(round(estimatePI(1000000), 3))

