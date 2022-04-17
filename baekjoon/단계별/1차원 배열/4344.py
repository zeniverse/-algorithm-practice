for _ in range(int(input())):
    n, *arr = map(int, input().split())
    avg = sum(arr)/n

    count = 0

    for i in arr:
        if i > avg:
            count += 1

    print("{:0.3f}%".format((count/n)*100))

