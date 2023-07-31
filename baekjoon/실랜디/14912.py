n, d = map(int, input().split())
cnt = 0

for num in range(1, n + 1):
    num = str(num)
    cnt += num.count(str(d))

print(cnt)