
def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if stk and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1

    return stk or [-1]
        
arr = [0, 1, 1, 1, 0]
print(solution(arr))