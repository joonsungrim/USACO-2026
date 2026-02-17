with open("revegetate.in", "r") as f:
    N, M = map(int, f.readline().split())
    num_list = [[] for _ in range(N)]
    food_list = [[1,2,3,4] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, f.readline().split())
        num_list[a-1].append(b-1)
        num_list[b-1].append(a-1)
ans = ''
for i in range(N):
    food = food_list[i][0]
    ans += str(food)
    for j in num_list[i]:
        if food in food_list[j]:
            food_list[j].remove(food)
with open("revegetate.out", "w") as f:
    f.write(ans + "\n")