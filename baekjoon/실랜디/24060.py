import sys
input = sys.stdin.readline

res = []

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = (len(arr) + 1)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j = 0, 0
    arr2 = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr2.append(left[i])
            res.append(left[i])
            i += 1
        else:
            arr2.append(right[j])
            res.append(right[j])
            j += 1

    while i < len(left):
        arr2.append(left[i])
        res.append(left[i])
        i += 1

    while j < len(right):
        arr2.append(right[j])
        res.append(right[j])
        j += 1

    return arr2

n, k = map(int, input().split())
lst = list(map(int, input().split()))
res = []
merge_sort(lst)

if len(res) < k:
    print(-1)
else:
    print(res[k - 1])