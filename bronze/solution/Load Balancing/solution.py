with open("balancing.in", "r") as fin:
    N, B = list(map(int, fin.readline().split()))
    x_list = []
    y_list = []
    crd_list = []
    for _ in range(N):
        x, y = list(map(int, fin.readline().split()))
        x_list.append(x)
        y_list.append(y)
        crd_list.append([x, y])
x_list.sort()
y_list.sort()
x_lines = []
y_lines = []
if x_list[N//2] - 1 > 0:
    x_lines.append(x_list[N//2] - 1)
if x_list[N//2] + 1 <= B:
    x_lines.append(x_list[N//2] + 1)
if y_list[N//2] - 1 > 0:
    y_lines.append(y_list[N//2] - 1)
if y_list[N//2] + 1 <= B:
    y_lines.append(y_list[N//2] + 1)
ans_list = []
for i in x_lines:
    for j in y_lines:
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for loc in crd_list:
            if loc[0] > i:
                if loc[1] > j:
                    q1 += 1
                else:
                    q4 += 1
            else:
                if loc[1] > j:
                    q2 += 1
                else:
                    q3 += 1
        ans = max([q1, q2, q3, q4])
        ans_list.append(ans)
with open("balancing.out", "w") as fout:
    fout.write(str(min(ans_list)) + "\n")