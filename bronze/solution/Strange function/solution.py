inp_am = int(input())
for _ in range(inp_am):
    num = int(input())
    ans = 0
    cur = 0
    while num != 0 and len(str(num)) != 0:
        cur = 0
        for i in list(str(num)):
            if int(i) == 0 or int(i) == 1:
                pass
            else:
                cur = 1
                break
        if cur == 0:
            num -= 1
            ans += 1
        else:
            len_num = len(list(str(num)))
            new_num = ''
            for i in range(len_num):
                if int(list(str(num))[i]) % 2 == 0:
                    new_num += '0'
                else:
                    new_num += '1'
            ans += 1
            list_new = list(new_num)
            for _ in range(len_num):
                if int(list_new[0]) == 0:
                    list_new.pop(0)
                else:
                    break
            new_num = ''
            for i in list_new:
                new_num += i
            if len(new_num) == 0:
                num = 0
            else:
                num = int(new_num)
    print(ans)