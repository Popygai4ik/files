import math

c = 0
for x in range(-10, 1000):
    for y in range(-10, 1000):
        if x > 0 and (y < ((-math.sqrt(3)/3)*x + 111)) and(y > ((math.sqrt(3)/3)*x)) :
            c += 1
print(c)