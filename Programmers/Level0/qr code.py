
def solution(q, r, code):
    res = ''

    for i in range(len(code)):
        if i % q == r:
            res += code[i]
    return res


q, r = 3, 1
code = "qjnwezgrpirldywt"
print(solution(q, r, code))