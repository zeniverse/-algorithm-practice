import math

def solution(w,h):
    all = w * h
    repeat = math.gcd(w, h)
    width_repeat = w // repeat
    height_repeat = h // repeat

    cut = width_repeat + height_repeat - 1

    return all - (cut * repeat)

print(solution(8, 12))

# https://school.programmers.co.kr/questions/64956
