n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
res = sum(arr)

for i in range(2, n, 3):
    res -= arr[i]

print(res)
