T, k = list(map(int,input().split()))
for _ in range(T):
    moo_len = int(input())
    moo = list(input())
    letter = [moo[-1]]
    for i in range(moo_len-1,0,-1):
        if moo[i-1] == moo[i]:
            if moo[i] == 'M':
                letter.append('M')
            else:
                letter.append('M')
        else:
            if moo[i] == 'M':
                letter.append('O')
            else:
                letter.append('O')
    real_letter = ''
    for i in range(moo_len-1,-1,-1):
        real_letter += letter[i]
    print('YES')
    if k == 1:
        print(real_letter)