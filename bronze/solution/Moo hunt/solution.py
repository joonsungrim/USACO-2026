N,K = list(map(int,input().split()))
m_list = []
o_list = []
all_list = []
for _ in range(K):
    m,o1,o2 = list(map(int,input().split()))
    m_list.append(m)
    o_list.extend([o1,o2])
    all_list.append([m,o1,o2])
line = ''
for i in range(1,N+1):
    if m_list.count(i) < o_list.count(i):
        line += 'O'
    elif m_list.count(i) > o_list.count(i):
        line += 'M'
    else:
        line += 'M'
point = 0
alr_list = []
for i in all_list:
    if line[i[0]-1] == 'M' and line[i[1]-1] == 'O' and line[i[2]-1] == 'O':
        point += 1
case = 1
line = list(line)
for i in range(N):
    f_point = 0
    if line[i] == 'M':
        line[i] = 'O'
        for j in all_list:
            if line[j[0]-1] == 'M' and line[j[1]-1] == 'O' and line[j[2]-1] == 'O':
                f_point += 1
        line[i] = 'M'
    if line[i] == 'O':
        line[i] = 'M'
        for j in all_list:
            if line[j[0]-1] == 'M' and line[j[1]-1] == 'O' and line[j[2]-1] == 'O':
                f_point += 1
        line[i] = 'O'
    if f_point == point:
        case += 1
print(point,case)