import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

counter = [0] * (max(arr) + 1)
res = 0

while end < n:
    if counter[arr[end]] < k:
        counter[arr[end]] += 1
        end += 1
    else:
        counter[arr[start]] -= 1
        start += 1

    res = max(res, end - start)

print(res)