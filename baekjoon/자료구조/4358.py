from collections import defaultdict
import sys

arr = defaultdict(int)
count = 0 

while True:
    tree = sys.stdin.readline().strip()

    if not tree:
        break

    arr[tree] += 1
    count += 1

for key in sorted(arr.keys()):
    print("{0} {1:.4f}".format(key, arr[key] / count * 100))