n1, n2 = map(int, input().split())
arr1 = list(input())[::-1]
arr2 = list(input())
T = int(input())

arr = arr1 + arr2

for _ in range(T):
    idx = 0
    while idx < n1 + n2 - 1:
        if arr[idx] in arr1 and arr[idx + 1] in arr2:
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            idx = idx + 2
        else:
            idx += 1

print("".join(arr))

