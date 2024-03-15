n = int(input())
v = list(map(int, input().split()))
v.reverse()

res = 1
tmp = 1

for i in range(1, n):
    if tmp < v[i]:
        tmp += 1
    elif tmp > v[i]:
        tmp = v[i]
    res += tmp

print(res)