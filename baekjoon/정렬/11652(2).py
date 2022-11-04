from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

tmp = Counter(arr).most_common()
tmp = sorted(tmp, key=lambda x:(-x[1], x[0]))
print(tmp[0][0])