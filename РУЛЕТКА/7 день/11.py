s = open('24_OjpdJLm.txt').readline()

max_res = ''
for i in range(len(s)):
    for j in range(i+ 1, len(s) -1):
        strika = s[i:j]
        if strika == strika[::-1] and len(strika) > len(max_res):
            max_res = strika

print(max_res)


max_pal = ''
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > len(max_pal):
            max_pal = sub

print(f'Самая длинная палиндромная подстрока: {max_pal}')
print(f'Её длина: {len(max_pal)}')
