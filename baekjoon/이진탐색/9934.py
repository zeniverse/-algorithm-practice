import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(n)]

def makeTree(arr, level):
    mid = len(arr) // 2
    tree[level].append(arr[mid])

    if len(arr) == 1:
        return

    makeTree(arr[:mid], level + 1)
    makeTree(arr[mid + 1:], level + 1)

makeTree(arr, 0)

for i in range(n):
    print(*tree[i])


