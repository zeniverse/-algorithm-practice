import sys

arr = list(sys.stdin.readline().strip())

for i in range(9, -1, -1):
    for j in range(len(arr)):
        if arr[j] == str(i):
            print(i, end="")
