f = open('6 - 24 .txt')
s = f.readline()
s = s.replace('**', '* *').replace('**', '* *')
s = s.replace('++', '+ +').replace('++', '+ +')
s = s.replace('+*', '+ *').replace('+*', '+ *')
s = s.replace('*+', '* +').replace('*+', '* +')
a = s.split()
res = ''
for x in a:
    x2 = x[:]
    if x[0] in '+*':
        x2 = x2[1:]
    if x[-1] in '+*':
        x2 = x2[:-1]
    x3 = x2.split('+')
    arf = ''
    for pod_sun in x3:
        if len(pod_sun) > 0 and eval(pod_sun) == 0:
            arf+= pod_sun + '+'
        elif len(pod_sun)> 0:
            if '0*' in pod_sun:
                arf = pod_sun[pod_sun.index('0*'):]+'+'
            elif pod_sun[-1] == '0':
                arf = '0+'
            else:
                arf = ''
        else:
            arf = ''
        res = max(res,arf,key=len)
print(len(res))
print(res)