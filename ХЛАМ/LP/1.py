num = int(input())
Max = 1537
n = r = num - 1
l = -1
while l < r - 1:
    m = (l + r) // 2
    if n - 5 * m < Max:
        r = m
    else:
        l = m
s = r
n -= 5 * s
distan = [0] + [-1] * Max
jumps = [3, 4, 5]
q = [0]
while q:
    d = q.pop()
    for i in range(3):
        if d + jumps[i] < Max and distan[d + jumps[i]] == -1:
            distan[d + jumps[i]] = distan[d] + 1
            q.append(d + jumps[i])
print(-1 if distan[n] == -1 else s + distan[n])
