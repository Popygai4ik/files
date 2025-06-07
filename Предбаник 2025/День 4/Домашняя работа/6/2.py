from math import sqrt

c= 0
for x in range(-1000,1000):
    for y in range(-1000,1000):
        if x > 0 and y>(sqrt(3)/3)*x and y < -(sqrt(3)/3)*x + 111:
            c+=1
print(c)