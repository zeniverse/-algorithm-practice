import math

k, d = 2, 4

def solution(k, d):
    res = 0

    for x in range(0, d + 1, k):
        # 원의 방정식을 생각해보면 되는데 (X^2 + Y^2 = d^2)
        # 이에 따르면 y = math.sqrt(d^2 - x^2) 가 된다.
        
        # 그렇다면 x를 기준으로 x가 0 일땐 y의 범위는
        # y <= math.sqrt(4^2 - 0^2) ----> y <= 4 (0, 1, 2, 3, 4) 가 된다.
        # 하지만 y의 값과 x의 값은 모두 k의 배수여야 하기 때문에
        # 실제로 x가 0일때 가능한 y의 값은 (0, 2, 4) 가 된다.
        # 위의 과정을 수식으로 나타내면 아래와 같아짐!
        res_d = math.floor(math.sqrt(d*d - x*x))
        res += (res_d // k) + 1


    return res

print(solution(k, d))