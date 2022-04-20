from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
mid = len(arr)//2
val = Counter(arr).most_common()


print(round(sum(arr)/n))
print(arr[mid])

if len(arr) > 1:
    if val[0][1] == val[1][1]:
        print(val[1][0])
    else:
        print(val[0][0])
else:
    print(val[0][0])

print(max(arr) - min(arr))
