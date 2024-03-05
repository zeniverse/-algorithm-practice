import bisect

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    count = 0

    for i in arr_a:
        count += bisect.bisect(arr_b, i - 1)

    print(count)