from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)

for _ in range(n):
    dict[int(input().rstrip())] += 1


dict = sorted(dict.items(), key=lambda x:(-x[1], x[0]))
print(dict)
print(dict[0][0])
