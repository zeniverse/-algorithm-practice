n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = []

for i in range(0, len(arr)//2):
    res.append(arr[i] + arr[-(i + 1)])

print(min(res))