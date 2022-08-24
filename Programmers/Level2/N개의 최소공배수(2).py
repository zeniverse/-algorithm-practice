
import math

arr = [1,2,3]

def solution(arr):
    res = arr[0]

    for i in arr:
        res = (res * i) // math.gcd(res, i)

    return res

print(solution(arr))