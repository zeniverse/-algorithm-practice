

def solution(n, m, section):
    res = 0
    now = 0

    for i in section:
        if i > now:
            res += 1
            now = i + m - 1

    return res

n, m = 16, 4
section = [2, 3, 15, 16]

print(solution(n, m, section))
