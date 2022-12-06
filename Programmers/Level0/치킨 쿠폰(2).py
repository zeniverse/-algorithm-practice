
chicken = 1081

def solution(chicken):
    res = 0

    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        res += chicken
        chicken += mod
        
    return res

print(solution(chicken))
