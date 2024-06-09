from collections import Counter

X, Y = "12321", "42531"

def solution(X, Y):
    res = Counter(X) & Counter(Y)
    res = sorted(res.items(), key = lambda x: -int(x[0]))

    if not res:
        return "-1"
    
    if res[0][0] == "0":
        return "0"
    
    arr = []
    for num, cnt in res:
        arr.append(num * cnt)

    return "".join(arr)


print(solution(X, Y))