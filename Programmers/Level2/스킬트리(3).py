
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

res = 0

for skills in skill_trees:
    tmp = ''

    for i in skills:
        if i in skill:
            tmp += i
    
    if tmp == skill[0:len(tmp)]:
        res += 1

print(res)