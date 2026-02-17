with open("lineup.in", "r") as f:
    sen = int(f.readline())
    name_list = ['Beatrice','Belinda','Bella','Bessie','Betsy','Blue','Buttercup','Sue']
    com_list = {'Beatrice':0,'Belinda':0,'Bella':0,'Bessie':0,'Betsy':0,'Blue':0,'Buttercup':0,'Sue':0}

    for _ in range(sen):
        com = f.readline().split()
        sup = com[0]
        main = com[-1]
        std_idx = name_list.index(main)
        chg_idx = name_list.index(sup)
        if com_list[main] == 0:
            if com_list[sup] == 0:
                name_list.remove(sup)
                name_list.insert(std_idx + 1,sup)
            else:
                fri_name = name_list[chg_idx + 1]
                name_list.pop(chg_idx + 1)
                name_list.remove(sup)
                name_list.insert(std_idx + 1,sup)
                name_list.insert(std_idx + 2,fri_name)
        else:
            if com_list[sup] == 0:
                name_list.remove(sup)
                name_list.insert(std_idx,sup)
            else:
                fri_name = name_list[chg_idx + 1]
                name_list.pop(chg_idx + 1)
                name_list.remove(sup)
                name_list.insert(std_idx,sup)
                name_list.insert(std_idx,fri_name)
        com_list[main] += 1
        com_list[sup] += 1

with open("lineup.out", "w") as f:
    for i in name_list:
        f.write(i + "\n")