# 문제 요약
# input으로 숫자가 여러개 들어오는데 그 순서대로 만들어진 리스트를 그 리스트가 sort된 형태로 바꾸려고 한다
# 각 숫자들의 위치들을 바꾸면서 리스트를 수정하려 한다
# 숫자들의 위치를 바꿔서 목적을 이룰 수 있는 가장 적은 횟수를 구해야 한다

cow_amount = int(input())
farm = []
for _ in range(cow_amount):
    cow_num = int(input())
    farm.append(cow_num)
farm_sort = []
for i in farm:
    farm_sort.append(i)
farm_sort.sort()
change_list = []
idx_list = []
for i in range(cow_amount):
    if farm[i] != farm_sort[i]:
        change_list.append(i)
for i in range(cow_amount):
    idx = farm_sort.index(farm[i])
    while idx in idx_list:
        idx += 1
    idx_list.append(idx)
ans = len(change_list) - 1
if ans < 0:
    ans = 0
minus = 0
for i in change_list:
    if i == idx_list[idx_list[i]]:
        minus += 1
minus = int(minus / 2) - 1
if minus < 0:
    minus = 0
ans -= minus
print(ans)