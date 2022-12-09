from itertools import combinations

number = [-1, 1, -1, 1]

def solution(number):
    res = 0

    for combi in combinations(number, 3):
        if sum(combi) == 0:
            res += 1

    return res


print(solution(number))