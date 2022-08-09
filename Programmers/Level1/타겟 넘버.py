numbers = [1, 1, 1, 1, 1]
target = 3

res = [0]

def dfs(i, num, arr):
    if i == len(arr):
        if num == target:
            res[0] += 1
        return

    v = arr[i]
    dfs(i + 1, num + v, arr)
    dfs(i + 1, num - v, arr)

dfs(0, 0, numbers)

print(res)

    