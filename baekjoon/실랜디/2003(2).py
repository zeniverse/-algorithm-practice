import sys
inpyt = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pref_sum = [0] * (n + 1)

for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

start, end = 0, 0
res = 0

while start < n:
    total = pref_sum[end + 1] - pref_sum[start]

    if total == m:
        res += 1

    if total <= m:
        end += 1
        if end >= n:
            break
    else:
        start += 1

print(res)