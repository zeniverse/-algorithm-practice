import copy

def solution(arr):
    res = 0
    while True:
        cal_arr = copy.deepcopy(arr)
        
        for i in range(len(arr)):
            if cal_arr[i] >= 50 and cal_arr[i] % 2 == 0:
                cal_arr[i] //= 2
            elif cal_arr[i] < 50 and cal_arr[i] % 2:
                cal_arr[i] = (cal_arr[i] * 2)+ 1

        if arr == cal_arr:
            return res
        else:
            arr = cal_arr
            res += 1
            

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))