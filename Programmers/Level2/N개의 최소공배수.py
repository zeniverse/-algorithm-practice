
import math


arr = [1,2,3]


def solution(arr):
    if len(arr) == 1:
        return arr[0]

    lcm = (arr[0] * arr[1]) // math.gcd(arr[0], arr[1])

    for i in range(2, len(arr)):
        lcm = (lcm * arr[i]) // math.gcd(lcm, arr[i])

    return lcm

print(solution(arr))