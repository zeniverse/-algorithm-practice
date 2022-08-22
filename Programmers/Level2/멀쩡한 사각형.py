import math

def solution(w,h):
    return (w*h)-(w+h-math.gcd(w,h))

print(solution(8, 12))

# https://leedakyeong.tistory.com/135#comment16270807
# 자세한 설명은 이 블로그에 나와있음