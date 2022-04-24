arr = list(map(int, input().split()))
res = ""

if arr[0] < arr[1]:
    for i in range(1, 7):
        if arr[i] > arr[i + 1]:
            res = "mixed"
            break
        else:
            res = "ascending"
else:
    for i in range(1, 7):
        if arr[i] < arr[i + 1]:
            res = "mixed"
            break
        else:
            res = "descending"

print(res)

