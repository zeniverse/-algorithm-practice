
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    adj = [0 for _ in range(n + 1)]

    for _ in range(n - 1):
        p, c = map(int, input().split())
        adj[c] = p

    a, b = map(int, input().split())

    a_parent = [a]
    b_parent = [b]

    while adj[a]:
        a_parent.append(adj[a])
        a = adj[a]

    while adj[b]:
        b_parent.append(adj[b])
        b = adj[b]
        
    a_level = len(a_parent) - 1
    b_level = len(b_parent) - 1

    while a_parent[a_level] == b_parent[b_level]:
        a_level -= 1
        b_level -= 1

    print(a_parent[a_level + 1])