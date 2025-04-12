import re
s = open('t').readline()
res = re.findall("[123456789][1203456789A]*", s)
print(max(res, key=len))
print(len(max(res, key=len)))