hp = 24

def solution(hp):
    res = 0

    for i in [5, 3]:
        res += hp // i
        hp = hp % i

    return res + hp

print(solution(hp))
