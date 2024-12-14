c = 0
for i in range(int('10000', 15), int('EEEEE', 15)+1):
    # print(shisl)
    if (int(i // 15 ** 4) % 2 == 0 and int(i // 15**3 % 15) % 3 == 0 and int(i // 15**2 % 15) % 2 == 0 and int(i // 15 % 15) % 3 == 0 and int(i % 15) % 2 == 0) or\
            (int(i // 15 ** 4) % 3 == 0  and int(i // 15**3 % 15) % 2 == 0 and int(i // 15**2 % 15) % 3 == 0 and int(i // 15 % 15) % 2 == 0 and int(i % 15) % 3 == 0):
        c +=1
print(c)
count = 0
for num in range(50625, 759375):
    d1 = num // 15**4
    d2 = num // 15**3 % 15
    d3 = num // 15**2 % 15
    d4 = num // 15 % 15
    d5 = num % 15
    check1 = (d1 % 2 == 0) and (d2 % 3 == 0) and (d3 % 2 == 0) and (d4 % 3 == 0) and (d5 % 2 == 0)
    check2 = (d1 % 3 == 0) and (d2 % 2 == 0) and (d3 % 3 == 0) and (d4 % 2 == 0) and (d5 % 3 == 0)
    if check1 or check2:
        count += 1
print(count)