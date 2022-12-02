array = [1, 2, 7, 10, 11]

def solution(array):
    array.sort()
    return array[len(array)//2]

print(solution(array))