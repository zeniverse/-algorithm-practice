
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

start = 1
end = (n - 1) * (1 + abs(arr[n] - arr[1]))
res = 0

while start <= end:
    mid = (start + end) // 2

    flag = False
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True

    while stack:
        k = stack.pop()

        if k == n:
            flag = True
            break

        for i in range(k + 1, n + 1):
            p = (i - k) * (1 + abs(arr[i] - arr[k]))

            if p <= mid and not visited[i]:
                stack.append(i)
                visited[i] = True

    if flag:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
