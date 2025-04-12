def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ne_vazrts(num):
    s = str(num)
    return s == ''.join(sorted(s))

a = [int(i) for i in open('11-17')]
mimi = min(i for i in a if is_prime(i))

res = []
middle_numbers = []

for i in range(len(a) - 2):
    n1, n2, n3 = a[i], a[i+1], a[i+2]
    cond1 = ne_vazrts(n1) and ne_vazrts(n2) and ne_vazrts(n3)
    cond2 = ((len(str(n1)) == 4) + (len(str(n2)) == 4) + (len(str(n3)) == 4) )<= 2
    cond3 = (n1 + n2 + n3) % mimi == 0
    if cond1 and cond2 and cond3:
        res.append((n1, n2, n3))
        middle_numbers.append(sorted([n1, n2, n3])[1])

print(len(res), max(middle_numbers))
