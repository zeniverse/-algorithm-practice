
def solution(a, d, included):
    res = 0
    for i in range(len(included)):
        if included[i]:
            res += a + (d * i)
    return res

a, d = 3, 4
included = [True, False, False, True, True]
print(solution(a, d, included))