k = int(input())
c = int(input())
res = []

for i in range(c):
    m, n = map(int, input().split())

    if m < n:
        if n - m - 1 >= k - n + 1:
            res.append(0)
        else:
            res.append(1)
    elif m > n:
        if m - n - 1 > k - m + 1:
            res.append(0)
        else:
            res.append(1)
    else:
        res.append(1)

for i in res:
    print(i)