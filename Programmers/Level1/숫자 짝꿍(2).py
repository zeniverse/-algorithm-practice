
X, Y = "12321", "42531"

def solution(X, Y):
    res = ''

    for i in range(9, -1, -1):
        res += str(i) * min(X.count(str(i)), Y.count(str(i)))

    if res == '':
        return "-1"
    elif len(res) == res.count('0'):
        return "0"
    else:
        return res

print(solution(X, Y))