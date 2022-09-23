import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]

for i in arr:
    sum_value += i
    prefix_sum.append(sum_value)

res = []
count = 0

while count + x <= n:
    res.append(prefix_sum[count + x] - prefix_sum[count])
    count += 1

if max(res) == 0:
    print('SAD')
else:
    print(max(res))
    print(res.count(max(res)))