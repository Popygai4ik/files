a = int(input())
m_num = 99999
for i in range(a):
    с = int(input())
    if с % 10 == 4 and с < m_num:
        m_num = с
print(m_num)