for x in '0123456789ABCD':
    for y in '0123456789ABCD':
        s1 = f'ABCD3{y}2{x}1'
        s2= f'192{x}9'
        if (int(s1, 14) + int(s2, 14)) % 107 == 0:
            print(x, y, (int(s1, 14) + int(s2, 14)) / 107)