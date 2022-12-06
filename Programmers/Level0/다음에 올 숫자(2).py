
common = [2, 4, 8]

def solution(common):
    a, b, c = common[:3]

    if (b-a) == (c-b):
        return common[-1] + (b-a)
    else:
        return common[-1] * (b//a)


print(solution(common))
