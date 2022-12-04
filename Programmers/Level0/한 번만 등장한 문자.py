from collections import defaultdict

s = 'hello'

def solution(s):
    dic = defaultdict(int)

    for i in s:
        dic[i] += 1

    res = ''
    for k, v in sorted(dic.items(), key=lambda x:x[0]):
        if v == 1:
            res += k

    return res


print(solution(s))
