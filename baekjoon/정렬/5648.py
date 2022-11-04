import sys
input = sys.stdin.readline

arr = []
while True:
    arr.extend(list(map(int, input().split())))

    if len(arr) == arr[0] + 1:
        break

n = arr[0]
arr = arr[1:]

for i in range(n):
    arr[i] = int(str(arr[i])[::-1])

arr.sort()
for i in arr:
    print(i)