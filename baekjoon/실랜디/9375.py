from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    dic = defaultdict(list)

    for _ in range(n):
        a, b = input().split()
        dic[b].append(a)

    res = 1
    for k in dic:
        res *= (len(dic[k]) + 1)
    print(res - 1)

    
