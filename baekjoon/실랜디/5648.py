import sys
input = sys.stdin.readlines()

n, *arr = input().split()

for i in range(int(n)):
    arr[i] = arr[i][::-1]

print(*sorted(list(map(int, arr))), end="\n")

