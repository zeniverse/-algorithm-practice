arr = [3,2,6]
divisor = 10

res = []

for i in arr:
    if i % divisor == 0:
        res.append(i)

res.sort()

if len(res) == 0:
    res.append(-1)

print(res)