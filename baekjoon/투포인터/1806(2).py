import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = sys.maxsize
left, right = 0, 0
summary = 0

while True:

    if summary >= m:
        res = min(res, right - left)
        summary -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        summary += arr[right]
        right += 1

if res == sys.maxsize:
    print(0)
else:
    print(res)