n, w = map(int, input().split())

coin = []
count = 0

for _ in range(n):
    coin.append(int(input()))

for i in range(n - 1):
    if coin[i] < coin[i + 1]:
        if w // coin[i] > 0:
            count = w // coin[i]
            w %= coin[i]

    elif coin[i] > coin[i - 1]:
        w += count * coin[i]
        count = 0

if count != 0:
    w += count * coin[-1]

print(w)
