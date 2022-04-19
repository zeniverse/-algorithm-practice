n = int(input())
arr = list(map(int, input().split()))

count = n

for i in arr:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count -= 1
                break
                
    elif i <= 1:
        count -= 1
        
print(count)