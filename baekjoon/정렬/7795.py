import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    count = 0

    for i in range(n):
        flag = False
        for j in range(m):
            if a[i] > b[j]:
                count += (m - j)
                flag = True
                break
        if not flag:
            break

    print(count)