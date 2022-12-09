from collections import defaultdict

X, Y = "12321", "42531"

def solution(X, Y):
    res = []

    x = defaultdict(int)
    y = defaultdict(int)

    for i in range(10):
        x[str(i)] = X.count(str(i))
        y[str(i)] = Y.count(str(i))

    for k, v in x.items():
        if v >= 1 and y[k] >= 1:
            for i in range(min(v, y[k])):
                res.append(k)

    res.sort(reverse=True)

    if not res:
        return "-1"
    elif res[0] == '0':
        return "0"
    else:
        return "".join(res)


print(solution(X, Y))