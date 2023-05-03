
def solution(arr, flag):
    res = []

    for i in range(len(flag)):
        if flag[i]:
            res += [arr[i]] * (arr[i] * 2)
        else:
            res = res[:-arr[i]]
    return res

arr =[3, 2, 4, 1, 3]
flag = [True, False, True, False, False]
print(solution(arr, flag))