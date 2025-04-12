def tre(n):
    res = ''
    while n > 0:
        res += str(n % 7)
        n = n // 7
    return res[::-1]
s = 5 * 3**1024 + 6 * 2**1010 + 7 * 6**743
print(bin(tre(s).count('6')))#1100100
def to_base7(n):
    res = ''
    while n > 0:
        res = str(n % 7) + res  # Добавляем в начало строки
        n //= 7
    return res

s = 5 * 3**1024 + 6 * 2**1010 + 7 * 6**743
count_sixes = to_base7(s).count('6')
print(bin(count_sixes)[2:])  # Убираем преф
