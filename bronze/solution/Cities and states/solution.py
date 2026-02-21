with open("citystate.in", "r") as fin:
    int_am = int(fin.readline())
    city_list = []
    initial_list = []
    ans = 0
    for _ in range(int_am):
        city, city_init = fin.readline().split()
        city_list.append(city)
        initial_list.append(city_init)
for i in range(int_am):
    chk_list = []
    cur_init = city_list[i][:2]
    for j in range(int_am):
        if initial_list[j] == cur_init:
            chk_list.append(j)
    for k in chk_list:
        if city_list[k][:2] == initial_list[i][:2]:
            ans += 1
with open("citystate.out", "w") as fout:
    fout.write(str(ans//2) + "\n")