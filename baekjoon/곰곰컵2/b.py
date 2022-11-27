
n = int(input())
res = set()
res.add("ChongChong")

for _ in range(n):
    a, b = input().split()
    
    if a in res:
        res.add(b)

    if b in res:
        res.add(a)

print(len(res))



