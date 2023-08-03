from collections import deque

n, m = map(int, input().split())
arr = deque([i for i in range(1, n + 1)])
index = list(map(int, input().split()))

count = 0
for num in index:
    while True:
        if arr[0] == num:
            arr.popleft()
            break
        else:
            if arr.index(num) <= len(arr)//2:
                arr.rotate(-1)
                count += 1
            else:
                arr.rotate(1)
                count += 1

print(count)
        
