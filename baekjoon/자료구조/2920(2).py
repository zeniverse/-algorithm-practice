arr = list(map(int, input().split()))

ascending = True
descending = True

for i in range(7):
    if arr[i] < arr[i + 1]:
        descending = False
    elif arr[i] > arr[i + 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")