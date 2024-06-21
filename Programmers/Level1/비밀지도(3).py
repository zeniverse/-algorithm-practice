n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        arr = bin(arr1[i] | arr2[i])
        arr = arr[2:].zfill(n)
        arr = arr.replace('1', '#').replace('0', ' ')
        answer.append(arr)
        
    return answer

print(solution(n, arr1, arr2))










