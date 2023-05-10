
def solution(arr):
    stk = []
    i = 0

    while len(arr) > i:
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk


arr = [1, 4, 2, 5, 3]
print(solution(arr))