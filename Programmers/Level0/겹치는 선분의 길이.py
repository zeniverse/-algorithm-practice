from collections import defaultdict

lines = [[0, 5], [3, 9], [1, 10]]

def solution(lines):
    dic = defaultdict(int)
    res = 0

    for line in lines:
        for i in range(line[0], line[1]):
            dic[i] += 1

    for k, v in dic.items():
        if v >= 2:
            res += 1

    return res
    

print(solution(lines))