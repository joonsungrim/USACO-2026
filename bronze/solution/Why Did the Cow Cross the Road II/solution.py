am_list = [[] for _ in range(26)]
act_list = []
with open("circlecross.in", "r") as fin:
    s = fin.readline().strip()
for i in list(s):
    if ord(i) - 97 not in act_list:
        act_list.append(ord(i) - 65)
    else:
        act_list.remove(ord(i) - 65)
    for j in act_list:
        if ord(i) - 65 == j:
            pass
        elif i not in am_list[j]:
            am_list[j].append(i)
        else:
            am_list[j].remove(i)
ans = 0
for i in am_list:
    ans += len(i)
with open("circlecross.out", "w") as fout:
    fout.write(str(int(ans / 2)) + "\n")