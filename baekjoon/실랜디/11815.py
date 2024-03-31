n = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num == (int(num ** 0.5) ** 2):
        print(1, end=" ")
    else:
        print(0, end=" ")
