
def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])

    return stk


arr = [1, 4, 2, 5, 3]
print(solution(arr))