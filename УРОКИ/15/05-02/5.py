q = list(range(20,38+1))
p = list(range(7,15+1))
# a = list(range(1,100))
a = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
for x in range(1,100):
    if (((not(x in p) ) <= (x in q)) or (not(x in a))) == False:
        # a.remove(x)
        print('1')
print(a)
