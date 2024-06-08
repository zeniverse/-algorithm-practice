
food = [1, 3, 4, 6]

def solution(food):
    res = ''

    for idx, n in enumerate(food[1:]):
        res += str(idx + 1) * (n // 2)
            
    return res + "0" + res[::-1]

print(solution(food))