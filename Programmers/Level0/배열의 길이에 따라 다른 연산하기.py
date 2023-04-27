
def solution(arr, n):
    s = 0

    if not len(arr) % 2:
        s = 1
    
    for i in range(s, len(arr), 2):
        arr[i] += n
        
    return arr

arr = [49, 12, 100, 276, 33]
n = 27
print(solution(arr, n))