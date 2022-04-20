import sys

n = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    div_num = list(map(int, str(i)))
    res = i + sum(div_num)

    if res == n:
        print(i)
        break

    if i == n:
        print(0)


