# def f(a,x,y):
#     return ((y > 250) or (x > 75) or ((5*x - 3*y) < a))
#
def f(a, x, y):
    return ((y > 250) or (x > 75) or ((5 * x - 3 * y) < a))
for a in range(0,400):
    for x in range(1,1000):
        for y in range(1,1000):
            if f(a,x,y) == False:
                break
        if f(a, x, y) == False:
            break
    else:
        print(a)
        break


for a in range(1000):  # Перебираем A
    for x in range(1, 1000):  # x от 1 до 75
        for y in range(1, 1000):  # y от 1 до 250
            if not f(a, x, y):  # Если хоть раз False, значит A не подходит
                break
        if not f(a, x, y):  # Если хоть раз False, значит A не подходит
            break
    else:
        print(a)  # Нашли минимальное A
        break
