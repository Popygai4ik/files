from random import randint, random
list = []
for i in range(20):
    a = randint(100, 1000)
    list.append(a)
sum1 = sum(list[:10])
sum2 = sum(list[10:])
print('Сумма 1:', sum1)
print('Сумма 2:', sum2)