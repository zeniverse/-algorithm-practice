
storey = 2554

def calc(N, storey):
    res = 0

    while storey > 0:
        x = storey % 10
        storey //= 10

        if x >= N:
            res += (10 - x)
            storey += 1
        else:
            res += x

    return res

def solution(storey):
    
    return min(calc(5, storey), calc(6, storey))

print(solution(storey))