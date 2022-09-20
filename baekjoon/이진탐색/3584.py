
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr_x = []
arr_y = []

def dfs(x, arr):
    arr.append(x)
    for i in adj[x]:
        dfs(i, arr)

for _ in range(int(input())):
    n = int(input())
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[b].append(a)

    x, y = map(int, input().split())

    dfs(x, arr_x)
    dfs(y, arr_y)
    
    for i in arr_x:
        if i in arr_y:
            print(i)
            break

    arr_x = []
    arr_y = []