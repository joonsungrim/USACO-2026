sid = int(input())
line_list = []
idx_list = []
for _ in range(sid):
    line = list(map(int,list(input())))
    line_list.append(line)
    i_idx = 0
    zer_list = []
    one_list = []
    for i in line:
        if i == 0:
            zer_list.append(i_idx)
        else:
            one_list.append(i_idx)
        i_idx += 1
    idx_list.append([zer_list,one_list])
print(line_list)
print(idx_list)