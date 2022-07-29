import math

left = 24
right = 27

res = 0

for i in range(left, right + 1):
    if int(math.sqrt(i)) == math.sqrt(i):
        res -= i
    else:
        res += i

print(res)