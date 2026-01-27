# 문제 요약
# There are 7 cows in farm and each cow provide milk several times.
# We have to find a cow that providse the milk the second least.
# However, if all cows provide the same amount of milk, we should print "Tie".

input_amount = int(input())
farm = {}
farm_len = 0
for _ in range(input_amount):
    name, milk = input().split()
    milk = int(milk)
    if name in farm:
        farm[name] += milk
    else:
        farm[name] = milk
        farm_len += 1
name_list = list(farm.keys())
milk_list = list(farm.values())
min_milk = min(milk_list)
ans_val = max(milk_list)
if min_milk == ans_val:
    print("Tie")
else:
    for i in range(farm_len):
        if milk_list[i] > min_milk:
            if milk_list[i] < ans_val:
                ans_val = milk_list[i]
    ans_loc = milk_list.index(ans_val)
    print(name_list[ans_loc])