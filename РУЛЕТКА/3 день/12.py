s = open('12-24').readline().replace('FX', "F_X").split('_')
r = 0
for i in range(len(s)-540):
    word = ''.join(s[i:i+541])
    r = max(r,len(word))
print(r)