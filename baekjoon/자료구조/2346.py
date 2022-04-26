n = int(input())
arr = list(map(int, input().split()))

for i, num in enumerate(arr, start=1):
    arr[i - 1] = (i, num)

index = 0 

while True:

    paper = arr[index][1]
    print(arr.pop(index)[0], end = " ")

    if len(arr) == 0:
        break

    if paper >= 0:
        index = (index + paper -1) % len(arr)
    else:
        index = (index + paper) % len(arr)
