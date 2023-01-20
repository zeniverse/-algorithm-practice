
storey = 2554

def solution(storey):
    res = 0
    
    while storey:
        remainder = storey % 10

        # 6 - 9
        if remainder > 5:
            res += (10 - remainder)
            storey += 10

        # 0 - 4
        elif remainder < 5:
            res += remainder
        
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            res += remainder

        storey //= 10

    return res

print(solution(storey))