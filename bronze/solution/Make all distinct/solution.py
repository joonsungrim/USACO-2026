inp_am = int(input())
for _ in range(inp_am):
    ans = 0
    N,K = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    if K < 0:
        n_K = K * -1
    else:
        n_K = K
    num_list = [[] for _ in range(n_K)]
    for i in arr:
        rem = i % n_K
        num_list[rem].append(i)
    if K > 0:
        for j in num_list:
            len_j = len(j)
            for i in range(1,len_j):
                if j[i] <= j[i-1]:
                    plus = (j[i-1] - j[i]) // K + 1
                    j[i] += K * plus
                    ans += plus
    else:
        n_K = K * -1
        for j in num_list:
            j.reverse()
            len_j = len(j)
            for i in range(1,len_j):
                if j[i] >= j[i-1]:
                    plus = (j[i] - j[i-1]) // n_K + 1
                    j[i] += K * plus
                    ans += plus
    print(ans)