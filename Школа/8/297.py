from  itertools import  *
def prome(n):
    if n == 1:
        return True # False
    for x in range(2, n):

        if n % x == 0:
            return False
    return True
c = 0
for i in product('01234567', repeat=5):
    w = ''.join(i)
    flsg = False
    if w[0] in '0':
        continue
    for j in range(5):
        for k in range(j +1, 5):
            # print(w)
            if w[k] != w[j] and prome(int(w[k]) + int(w[j])):
                flsg = True
    if flsg:
         c+=1
print(c)


