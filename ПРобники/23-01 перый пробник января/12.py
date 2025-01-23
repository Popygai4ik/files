for n in range(0, 10000):
    s = '>' + '4' * 97 + '7' * 30 + '3' * n
    while '>4' in s or '>7' in s or '>3' in s:
        if '>4' in s:
            s = s.replace('>4', '37>', 1)
        if '>7' in s:
            s = s.replace('>7', '3>', 1)
        if '>3' in s:
            s = s.replace('>3', '437>4', 1)

    if int(s[:-1]) % 103 == 0:
        print(n)
