
food = [1, 3, 4, 6]

def solution(food):
    res = '0'

    for i in range(len(food) - 1, 0, -1):
        cnt = int(food[i]/2)

        while cnt > 0:
            res = str(i) + res + str(i)
            cnt -= 1
            
    return res

print(solution(food))