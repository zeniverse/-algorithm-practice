for _ in range(int(input())):
    h, w, n = map(int, input().split())

    count = 1


    while n > h:
        n -= h
        count += 1

    print(n * 100 + count)

    