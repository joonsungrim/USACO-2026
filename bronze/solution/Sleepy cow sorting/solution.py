with open("sleepy.in", "r") as f:
    cow_am = int(f.readline().strip())
    cow_ord = list(map(int, f.readline().split()))
fin_ord = sorted(cow_ord)
ans = 0
while cow_ord != fin_ord:
    fir_cow = cow_ord[0]
    if fir_cow == 1:
        big_idx = cow_ord.index(cow_am)
        cow_ord.insert(big_idx + 1, fir_cow)
        cow_ord.pop(0)
        ans += 1
    else:
        less_idx = cow_ord.index(fir_cow - 1)
        cow_ord.insert(less_idx + 1, fir_cow)
        cow_ord.pop(0)
        ans += 1
with open("sleepy.out", "w") as f:
    f.write(str(ans) + "\n")