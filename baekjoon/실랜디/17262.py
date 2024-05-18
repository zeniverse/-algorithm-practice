n = int(input())
arr = []

for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

a = sorted(arr, key = lambda x: x[0])
b = sorted(arr, key = lambda x: x[1])

res = a[-1][0] - b[0][1]

if res <= 0:
    print(0)
else:
    print(res)