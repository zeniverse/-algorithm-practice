n = int(input())
Entry = {input().rstrip() : i for i in range(n)}
Exit = list(int(Entry[input().rstrip()]) for _ in range(n))

res = 0
for i in range(n):
    for j in range(i, n):
        if Exit[i] > Exit[j]:
            res += 1
            break
print(res)