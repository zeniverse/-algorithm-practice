from itertools import permutations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for per in permutations(arr, n):
    flag = True
    m = 500
    for i in per:
        m += i
        m -= k

        if m < 500:
            flag = False
            break
    if flag:
        res += 1

print(res)
    
