import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

res = set()

def dfs(first, second, index):
    first.add(index)
    second.add(arr[index])

    if arr[index] in first:
        if first == second:
            res.update(first)
            return
        return
    return dfs(first, second, arr[index])


for i in range(1, n + 1):
    if i not in res:
        dfs(set(), set(), i)

res = list(res)
res.sort()
print(len(res))
print("\n".join(map(str,res)))