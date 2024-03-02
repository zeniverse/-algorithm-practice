for _ in range(int(input())):
    n = int(input())
    sum_ = sum(list(map(int, input().split())))
    count = 1

    while n >= sum_:
        count += 1
        sum_ *= 4

    print(count)