import math

balls = 5
share = 3

def solution(balls, share):
    return math.comb(balls, share)

print(solution(balls, share))

# combinations를 사용하면 시간 초과가 나옴 - 실제 조합을 생성함
# math.comb를 사용하면 통과함 - 실제 조합을 생성하지 않고 개수만 계산하므로 매우 빠름