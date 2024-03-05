
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    start = 0
    count = 0

    for i in range(n):
        while True:
            if start == m or arr_a[i] <= arr_b[start]:
                count += start
                break
            else:
                start += 1

    print(count)