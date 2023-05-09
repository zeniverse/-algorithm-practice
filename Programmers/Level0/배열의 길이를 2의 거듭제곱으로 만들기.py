
def solution(arr):
    
    while True:
        if (len(arr) & (len(arr) - 1)) == 0:
            return arr
        else:
            arr.append(0)
     

arr = [1, 2, 3, 4, 5, 6]
print(solution(arr))