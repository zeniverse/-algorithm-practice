angle = 45

def solution(angle):
    return (angle // 90) * 2 + (angle % 90 > 0) * 1

print(solution(angle))
