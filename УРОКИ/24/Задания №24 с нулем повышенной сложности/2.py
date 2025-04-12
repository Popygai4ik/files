s = open('t').readline()
import re
# re.findall(r'(?:0|[123456789ABCDE][0123456789ABCDE]*)(?:[+*](?:0|[123456789ABCDE][0123456789ABCDE]*))*', s)
res = re.findall(r"(?:0|[123456789ABCDE][0123456789ABCDE]*)(?:[*+](?:0|[123456789ABCDE][0123456789ABCDE]*))*", s)
ans = max(res, key=len)
pores = [x for x in ans if x in '+*']

ans_wout = ans.replace('+', '*').split('*')
ans_adekvat = [str(int(i, 15)) for i in ans_wout]
rtes = ''
for i in range(len(ans_adekvat) - 1):
    rtes += (ans_adekvat[i] + pores[i])
rtes += ans_adekvat[-1]
print(rtes)
print(sum((int(i) for i in str(eval(rtes)))))