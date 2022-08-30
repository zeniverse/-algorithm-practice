
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

res = 0

for skills in skill_trees:
    flag = True
    tmp = []
    for i in range(len(skill)):
        tmp.append(skills.find(skill[i]))
        print(skill[i], tmp)

        if (tmp[i - 1] > tmp[i] and tmp[i] != -1) or (tmp[i - 1] == -1 and tmp[i] != -1):
            flag = False
            break
        
    if flag:
        res += 1
        print(res)

print(res)

