c = []
for N in range(1, 1000):
    n = bin(N)[2:]
    srt = str(n)
    s_bina = [int(digit) for digit in str(n[2:])]
    smu = sum(s_bina)

    if smu % 2 == 0:
        srt = '1' + srt[:-2] + '01'
    else:
        srt = '0' + srt
        srt = '10' + srt[2:]
    res = int(srt, 2)
    if res > 48:
        c.append(N)
print(min(c))