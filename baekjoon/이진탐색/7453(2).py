
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []

ab = []
cd = []
res = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()

start = 0
end = len(cd) - 1

while start < len(ab) and end >= 0:
    tmp = ab[start] + cd[end]

    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1
    else:
        abLeft = bisect_left(ab, ab[start])
        abRight = bisect_right(ab, ab[start])

        cdLeft = bisect_left(cd, cd[end])
        cdRight = bisect_right(cd, cd[end])

        res += (abRight - abLeft) * (cdRight - cdLeft)
        start = abRight
        end = cdLeft - 1


print(res)