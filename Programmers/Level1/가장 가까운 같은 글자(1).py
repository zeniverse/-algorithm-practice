s = "footbar"

def solution(s):
    dic = dict()
    res = []

    for i in range(len(s)):
        if s[i] not in dic:
            res.append(-1)
        else:
            res.append(i - dic[s[i]])

        dic[s[i]] = i

    return res
    

print(solution(s))