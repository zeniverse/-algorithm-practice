import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        if x >= r1:
            y_min = 0
        else:
            y_min = math.ceil(math.sqrt(r1**2 - x**2))
        y_max = math.floor(math.sqrt(r2**2 - x**2))

    answer += y_max - y_min + 1

    return answer * 4