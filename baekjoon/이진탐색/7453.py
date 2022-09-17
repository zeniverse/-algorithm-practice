
import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []

ab = dict()
res = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        tmp = A[i] + B[j]

        if tmp not in ab:
            ab[tmp] = 1
        else:
            ab[tmp] += 1

for i in range(n):
    for j in range(n):
        tmp = -(C[i] + D[j])

        if tmp in ab:
            res += ab[tmp]

print(res)