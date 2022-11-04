from bisect import bisect_left
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    count = 0

    for i in a:
        tmp = bisect_left(b, i)
        count += tmp

    print(count)