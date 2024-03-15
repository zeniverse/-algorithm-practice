n, s = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))

l.sort()

res = 0
start = 0
end = len(l) - 1

while start <end:
    if l[start] + l[end] > s:
        end -= 1
    else:
        res += (end - start)
        start += 1

print(res)