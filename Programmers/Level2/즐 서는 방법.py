
from math import factorial

n = 3
k = 5

arr = [i for i in range(1, n + 1)]
res = []

while n != 0:
    case = factorial(n) // n

    passed = k // case
    k = k % case

    if k == 0:
        res.append(arr.pop(passed - 1))
    else:
        res.append(arr.pop(passed))

    n -= 1

print(res)