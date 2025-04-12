Q = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14}
P = {2, 4, 6, 7, 8, 10, 14}
a=list(range(1,100))

for x in range(1,1000):
    if ( ((x in P) <= (x in a)) and  ((x in a) <= (x in Q))) == False:
        a.remove(x)
print(sum(a))