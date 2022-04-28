import sys

n = int(sys.stdin.readline().strip())
top = list(map(int, sys.stdin.readline().strip().split()))
stack = []
res = [0] * n

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, top[i]))

print(*res)
