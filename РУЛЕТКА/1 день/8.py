for x in '012345678':
    s1 = int(f'2{x}{x}86', 9)
    s2 = int(f'72{x}38', 9)
    if (s1 + s2) % 14 == 0:
        print(x, (s1 + s2) // 14)
