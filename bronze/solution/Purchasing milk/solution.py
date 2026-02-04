N,Q = list(map(int,input().split()))
m_price = list(map(int,input().split()))
eff_list = []
amount = 1
eff_rank = []
for i in m_price:
    eff_list.append([i/amount,amount,i])
    amount *= 2
eff_list.sort()
for i in eff_list:
    eff_rank.append(i[1])
for _ in range(Q):
    buy = int(input())
    buy_list = []
    len_buy = 0
    for i in eff_rank:
        buy_list.append(buy // i)
        buy = buy % i
        len_buy += 1
        if buy == 0:
            break
    use = 0
    for i in range(len_buy):
        use += eff_list[i][2] * buy_list[i]
    print(int(use))