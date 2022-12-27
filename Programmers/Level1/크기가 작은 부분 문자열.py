
t = "10203"
p = "15"

def solution(t, p):

    res = 0

    for i in range(len(t) - (len(p) - 1)):
        if int(t[i:i + len(p)]) <= int(p):
            res += 1

    return res

print(solution(t, p))