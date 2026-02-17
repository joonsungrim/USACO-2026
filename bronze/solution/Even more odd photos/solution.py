list_len = int(input())
num_list = list(map(int,input().split()))
odd_list = []
even_list = []
for i in num_list:
    if i % 2 == 1:
        odd_list.append(i)
    else:
        even_list.append(i)
len_odd = len(odd_list)
len_even = len(even_list)
if len_odd == len_even:
    ans = len_odd * 2
elif len_odd < len_even:
    ans = len_odd * 2 + 1
else:
    while len_odd > len_even:
        len_odd -= 2
        len_even += 1
    if len_odd + 1 < len_even:
        len_even -= 1
    ans = len_odd + len_even
print(ans)