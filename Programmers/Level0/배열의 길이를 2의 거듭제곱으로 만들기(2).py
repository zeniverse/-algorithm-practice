
def solution(arr):
    
    length = len(arr)
    count = 0

    while length > 1:
        length = length / 2
        count += 1

    return arr + [-1] * (2 ** count - len(arr))
     

arr = [1, 2, 3, 4, 5, 6]
print(solution(arr))