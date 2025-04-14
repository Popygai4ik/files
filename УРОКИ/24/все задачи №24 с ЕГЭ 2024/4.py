f = open('24.4dz.txt')
s = f.readline()
import re
ios_ok = re.findall(r'[1-9][0-9]*(?:[*][1-9][0-9]*)*', s)
print(max(ios_ok,key=eval))
s = s.replace('+',' ').replace('**','* *').replace('**','* *')
s = s.replace(' *',' ').replace('* ',' ').replace('*0*',' ').replace(' 0*',' ').replace('*0 ',' ')
a = s.split()
print(len(str(eval(max(a,key=eval)))))