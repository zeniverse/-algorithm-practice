
n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
res = 0

for i in range(n - 1):
    if minPrice > price[i]:
        minPrice = price[i]

    res += (minPrice * dist[i])

print(res)

