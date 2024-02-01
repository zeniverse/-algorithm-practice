
n, k = map(int, input().split())
arr = []
res = 0

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr:
    if k >= i:
        res += k // i
        k %= i
        
        if k <= 0:
            break

print(res)
