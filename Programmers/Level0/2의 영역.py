
def solution(arr):
    res = list(filter(lambda x : arr[x] == 2, range(len(arr))))
    if res:
        return arr[res[0]:res[-1] + 1]
    else:
        return [-1]  

arr = [1, 2, 1, 2, 1, 10, 2, 1]
print(solution(arr))