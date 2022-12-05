
sides = [11, 7]

def solution(sides):
    res = 0
    sides.sort()
    max_num = sides[-1]
    for i in range(1, max_num + 1):
        if sides[0] + i > max_num:
            res += 1

    res += sum(sides) - max_num - 1

    return res


print(solution(sides))
