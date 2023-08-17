import sys
input = sys.stdin.readline

def merge_sort(arr, p, r):
    if p < r and count <= k:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global count, res

    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    i, t = p, 0

    while i <= r:
        arr[i] = tmp[t]
        count += 1
        if count == k:
            res = arr[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
res = -1
merge_sort(lst, 0, n - 1)
print(res)