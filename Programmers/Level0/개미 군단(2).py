hp = 24

def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

print(solution(hp))
