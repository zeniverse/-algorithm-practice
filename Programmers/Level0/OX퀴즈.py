
quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    res = []

    for q in quiz:
        ans = 0
        ans = eval(q.split(" = ")[0])
        if ans == int(q.split(" = ")[1]):
            res.append("O")
        else:
            res.append("X")

    return res

print(solution(quiz))
