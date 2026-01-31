# 문제 요약
# There is a list of numbers and we have to find how many patterns of [x,y,y] we can make with the list.
# We can't mix the order of the list. We can only delete the numbers so only three numbers remain.

len_moo = int(input())
moo = list(map(int,input().split()))
moo_amount = 0
one_num = []
don_num = []
for i in range(len_moo - 1,-1,-1):
    if moo[i] not in don_num:
        if moo[i] in one_num:
            one_num.remove(moo[i])
            don_num.append(moo[i])
            set_moo = set(moo[:i])
            moo_amount += len(set_moo)
            if moo[i] in set_moo:
                moo_amount -= 1
        else:
            one_num.append(moo[i])
print(moo_amount)