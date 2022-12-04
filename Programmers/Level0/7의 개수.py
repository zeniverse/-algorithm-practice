
array = [7, 77, 17]

def solution(array):
    res = 0

    for i in array:
        res += str(i).count('7')

    return res


print(solution(array))
