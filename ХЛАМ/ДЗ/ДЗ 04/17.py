import random

list = [random.randint(-100, 100) for i in range(10)]
print(list)
min_number = 0
min_index = 0

for i in range(len(list)):
    if list[i] % 10 == 5:
        if min_number == 0 or list[i] < min_number:
            min_number = list[i]
            min_index = i

if min_number != 0:
    print(f"Минимальное значение, десятичное окончание которого равно 5, это {min_number} на позиции {min_index}.")
else:
    print("нет")
