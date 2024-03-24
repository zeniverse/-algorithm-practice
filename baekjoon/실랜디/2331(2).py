n, m = map(int, input().split())
arr = [0] * 236197
count = 1

def cal(a, b):
    res = 0
    for i in str(a):
        res += int(i) ** b
    return res

def dfs(n, m, count, arr):
    if arr[n] != 0:
        return arr[n] - 1
    
    arr[n] = count
    count += 1
    res = cal(n, m)

    return dfs(res, m, count, arr)

print(dfs(n, m, count, arr))
