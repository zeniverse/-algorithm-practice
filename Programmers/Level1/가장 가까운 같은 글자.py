from collections import defaultdict

s = "footbar"

def solution(s):
    dic = defaultdict(int)
    res = []

    for i in range(len(s)):
        if dic[s[i]] == 0:
            dic[s[i]] = i + 1
            res.append(-1)
        else:
            res.append((i + 1) - dic[s[i]])
            dic[s[i]] = i + 1

    return res
    

print(solution(s))