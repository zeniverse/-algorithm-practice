import math

a = int(input())
b = int(input())

arr = [True for i in range(b + 1)]
res = []

for i in range(2, int(math.sqrt(b)) + 1):
    if arr[i]:
        j = 2

        while i * j <= b:
            arr[i * j] = False
            j += 1

for i in range(a, b + 1):
    if i > 1:
        if arr[i]:
            res.append(i)
            
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)
