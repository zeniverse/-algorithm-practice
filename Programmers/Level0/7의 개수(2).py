
array = [7, 77, 17]

def solution(array):
    return ''.join(map(str, array)).count('7')


print(solution(array))
