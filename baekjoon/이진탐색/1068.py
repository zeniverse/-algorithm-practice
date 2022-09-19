
import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2

    for i in range(n):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
del_node = int(input())
res = 0

dfs(del_node, arr)

for i in range(n):
    if arr[i] != -2 and i not in arr:
        res += 1

print(res)
