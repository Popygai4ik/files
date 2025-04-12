c = 0
for n in range(10999999,15000000):
    bini = bin(n)[2:]
    if sum(int(i) for i in str(n)) % 4 == 0:
        bini += '1'
    else:
        bini += '0'
    if sum(int(i) for i in str(int(bini,2))) % 4 == 0:
        bini += '1'
    else:
        bini += '0'
    if sum(int(i) for i in str(int(bini,2))) % 4 == 0:
        bini += '1'
    else:
        bini += '0'
    R = int(bini,2)
    print(f"N = {n}, R = {R}")

    if 23_456_789 <= R <= 98_765_432:
        c +=1
print(c)
# N = 8999999, R = 71999992 } N = 10999999, R = 87999994
#6067901 + 2000001 + 1345680