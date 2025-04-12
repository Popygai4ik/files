# def to23(start, stop):
#     if start == stop:
#         return 1
#     if start > stop:
#         return 0
#     if start<stop:
#         print(start)
#         num = int(str(start), 2)
#         k = str(num) + bin((num % 8))[2:]
#         return to23(start+1,stop) + to23(num,stop)
# print(to23(1, 190))
def to23(current, target):
    if current == target:
        return 1
    if len(current) > len(target):
        return 0

    num = int(current, 2)

    # Операция 1: +1 → в двоичный вид
    op1 = bin(num + 1)[2:]

    # Операция 2: приписать остаток от деления на 8 в двоичном виде
    op2 = current + bin(num % 8)[2:]

    return to23(op1, target) + to23(op2, target)

start = '1'
target = '10111110'
print(to23(start, target))
