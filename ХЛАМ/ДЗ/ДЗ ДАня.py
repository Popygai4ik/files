# 2
matrix = [
    [10, 20, 30],
    [4067, 567898, 6234],
    [1, 18, -10]
]

minimal_znasenie = 88003553535
maximal_znasenie = -88003553535
minimal_index = 0
maximal_index = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] > 0 and matrix[i][j] % 2 == 0:
            if matrix[i][j] < minimal_znasenie:
                minimal_znasenie = matrix[i][j]
                minimal_index = (i, j)
            if matrix[i][j] > maximal_znasenie:
                maximal_znasenie = matrix[i][j]
                maximal_index = (i, j)

if minimal_index != 0:
    print(f"Минимальный чётный положительный элемент: {minimal_znasenie} с индексом {minimal_index}")
else:
    print("В матрице нет чётных положительных элементов")

if maximal_index != 0:
    print(f"Максимальный чётный положительный элемент: {maximal_znasenie} с индексом {maximal_index}")
else:
    print("В матрице нет чётных положительных элементов")
# ДЗ ИЗ МЕЩА
stroka = "аббавввавв"
# s = "aaaabb"
maximal_dlina = 0
vrem_dlina = 1

for i in range(1, len(stroka)):
    if stroka[i] == stroka[i - 1]:
        vrem_dlina += 1
    else:
        maximal_dlina = max(maximal_dlina, vrem_dlina)
        vrem_dlina = 1

maximal_dlina = max(maximal_dlina, vrem_dlina)

print(f"Максимальная длина подцепочки: {maximal_dlina}")
