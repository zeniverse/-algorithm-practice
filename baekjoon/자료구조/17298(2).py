import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
res = [-1] * n

stack.append(0)
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]

    stack.append(i)

print(*res)