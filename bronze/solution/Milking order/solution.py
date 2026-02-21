with open("milkorder.in", "r") as fin:
    N, M, K = list(map(int, fin.readline().split()))
    loc_com = list(map(int, fin.readline().split()))
    arr = [0 for _ in range(N)]
    fix_list = []
    zer_list = [i for i in range(N)]
    for _ in range(K):
        num, idx = list(map(int, fin.readline().split()))
        arr[idx-1] = num
        fix_list.append(num)
        zer_list.remove(idx-1)
found = 0
arr_idx = 0
zer_am = 0
if 0 in arr:
    zer_idx = arr.index(0) + 1
ans = 0
loc_arr = 0
loc_idx = 0
for i in loc_com:
    if i in arr:
        loc_arr = 1
if loc_arr == 1:
    for i in arr:
        if found == 0:
            if i in loc_com:
                loc_idx = loc_com.index(i)
                for j in arr[:arr_idx]:
                    if j == 0:
                        zer_am += 1
                if zer_am > loc_idx:
                    ans = zer_idx
                else:
                    found = 1
        if found == 1:
            if i == 0:
                ans = arr_idx + 1
                break
        arr_idx += 1
else:
    for i in range(N):
        if loc_idx < M:
            if arr[i] == 0:
                if loc_com[loc_idx] == 1:
                    ans = i + 1
                    break
                else:
                    loc_idx += 1
        else:
            if arr[i] == 0:
                ans = i + 1
                break
with open("milkorder.out", "w") as fout:
    fout.write(str(ans) + "\n")