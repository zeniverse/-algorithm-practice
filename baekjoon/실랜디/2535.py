from collections import defaultdict

n = int(input())
arr = []
check = defaultdict(int)
count = 0

for _ in range(n):
    a, b, c = input().split()
    arr.append([a, b, int(c)])

arr.sort(key=lambda x:-x[2])

for i in range(n):
    if check[arr[i][0]] < 2:
        print(arr[i][0], arr[i][1])
        count += 1
    check[arr[i][0]] += 1

    if count == 3:
        break


    
