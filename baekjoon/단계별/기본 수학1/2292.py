n = int(input())
res = 1
cnt = 1

while res < n:
    res += 6 * cnt
    cnt += 1

print(cnt)

