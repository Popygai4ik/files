from random import randint
list = []
for i in range(10):
    a = randint(-2, 2)
    list.append(a)
print(list)
proz = 1
for i in list:
    if i != 0:
        proz *= i
print(proz)
