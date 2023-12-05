p, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

total = 0
for i in range(n): 
    if p < 200: 
        total += 1
        p += arr[i]
    else : 
        break
        
print(total)