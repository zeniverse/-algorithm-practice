
from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
power = []

for _ in range(n):
    t, p = input().split()
    title.append(t)
    power.append(int(p))

for _ in range(m):
    p = int(input())

    index = bisect_left(power, p)
    print(title[index])



    