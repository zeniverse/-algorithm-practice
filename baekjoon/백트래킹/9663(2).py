n = int(input())

res = 0
arr1 = [False] * n
arr2 = [False] * (2 * n)
arr3 = [False] * (2 * n)

def func(k):
    global res

    if k == n:
        res += 1
        return

    for i in range(n):
        if not (arr1[i] or arr2[i + k] or arr3[k - i + n - 1]):
            arr1[i] = arr2[k + i] = arr3[k - i + n - 1] = True
            func(k + 1)
            arr1[i] = arr2[k + i] = arr3[k - i + n - 1] = False

func(0)
print(res)
