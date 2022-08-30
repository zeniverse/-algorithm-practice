
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

res = 0

for skills in skill_trees:
    lst = list(skill)

    for s in skills:
        if s in skill:
            if s != lst.pop(0):
                break
    else:
        res += 1

print(res)
