s = open('t').readline()
s = s.replace('**','* *').replace('**','* *')
s = s.replace('++','+ +').replace('++','+ +')
s = s.replace('+*','+*').replace('+*','+ *')
s = s.replace('*+','* +').replace('*+','* +')
a = s.split()
max_arf = ''
for x in a:
    x2 = x[:]
    if x[0] in '+*':
        x2 = x2[1:]
    if x[-1] in '+*':
        x2 = x2[:-1]
    x3 = x2.split('+')
    arf = ''
    for posum in x3:
        if len(posum) > 0 and eval(posum) == 0:
            arf += posum + '+'
        elif len(posum) > 0:
            if '0*' in posum:
                arf = posum[posum.index('0*'):]+'+'
            elif posum[-1] == '0':
                arf = '0+'
            else:
                arf = ''
        else:
            arf = ''
        max_arf = max(max_arf,arf,key=len)
print(len(max_arf))
#125