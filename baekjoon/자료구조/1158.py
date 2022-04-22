n, k = map(int, input().split())
arr = list(range(1, n + 1))
res = []
num = k - 1

while len(arr):

    if num >= len(arr):
        num = num % len(arr)

    else:
        res.append(str(arr.pop(num)))
        num += k - 1

print('<', ', '.join(res), '>', sep='')