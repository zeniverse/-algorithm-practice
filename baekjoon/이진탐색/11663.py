
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(m):
    a, b = map(int, input().split())
    print(bisect_right(points, b) - bisect_left(points, a))

