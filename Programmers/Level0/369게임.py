
order = 3

def solution(order):
    res = 0

    for i in str(order):
        if i in ["3", "6", "9"]:
            res += 1

    return res

print(solution(order))
