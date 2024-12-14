from itertools import product
res= []
for i in product('CDO', repeat=5):
    res.append(i)
res.sort()
print(''.join(res[69]))