fibo = [0, 1]

for i in range(2, 46):
    fibo.append(fibo[i - 2] + fibo[i - 1])

for _ in range(int(input())):
    num = int(input())

    res = []

    for i in range(45, 0, -1):
        if fibo[i] <= num:
            res.append(fibo[i])
            num -= fibo[i]

            if num == 0:
                res.sort()
                print(*res)
                break