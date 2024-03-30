from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))
length = len(str(n))

while True:
    cand = list(product(arr, repeat=length))
    res = []

    for i in cand:
        tmp = int(''.join(map(str, i)))
        
        if tmp <= n:
            res.append(tmp)
        
    if len(res) >= 1:
        print(max(res))
        break
    else:
        length -= 1