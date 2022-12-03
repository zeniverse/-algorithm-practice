
cipher = "dfjardstddetckdaccccdegk"
code = 4

def solution(cipher, code):
    res = ''

    for i in range(code - 1, len(cipher), code):
        res += cipher[i]

    return res


print(solution(cipher, code))
