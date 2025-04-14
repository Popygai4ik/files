f = open('f9967a92-d26e-4dae-ba83-a907e608688f_24_new.txt')
s = f.readline()
s = s.replace('++','+ +').replace('++','+ +')
s = s.replace('**','* *').replace('**','* *')
s = s.replace('+*','+ *').replace('+*','+ *')
s = s.replace('*+','* +').replace('*+','* +')
a = s.split()
maxi = ''
for x in a:
    x2 = x[:]
    if x[0] in '+*':
        x2 = x2[1:]
    if x[-1] in '+*':
        x2 = x2[:-1]
    x3 = x2.split('+')
    arf = ''
    for pod_sum in x3:
        if len(pod_sum) > 0 and eval(pod_sum) == 0:
            arf += pod_sum + '+'
        elif len(pod_sum) > 0:
            if '0*' in pod_sum:
                arf = pod_sum[pod_sum.index('0*'):]+'+'
            elif pod_sum[-1] == '0':
                arf = '0+'
            else:
                arf = ''
        else:
            arf = ''
        maxi = max(maxi,arf,key=len)
print(len(maxi), maxi)