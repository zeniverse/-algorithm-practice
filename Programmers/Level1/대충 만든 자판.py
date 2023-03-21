from collections import defaultdict

def solution(keymap, targets):
    res = []
    dic = defaultdict(list)

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            dic[keymap[i][j]].append(j + 1)

    for k, v in dic.items():
        v.sort()

    for target in targets:
        ans = 0
        flag = False
        for word in target:
            if not dic[word]:
                res.append(-1)
                flag = True
                break
            else:
                ans += dic[word][0]
        if not flag:
            res.append(ans)

    return res

keymap = ["AA"]
targets = ["B"]

print(solution(keymap, targets))
