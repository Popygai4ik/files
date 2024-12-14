# 17?575*
for i in range(146, 10**8, 146):
    if str(i)[:2] == "17" and str(i)[3:6] == '575' and i % 146 == 0:
        print(i, i / 146)