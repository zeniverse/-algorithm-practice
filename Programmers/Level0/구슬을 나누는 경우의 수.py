import math

balls = 5
share = 3

def solution(balls, share):
    return math.factorial(balls) // (math.factorial(balls - share) * math.factorial(share))

print(solution(balls, share))
