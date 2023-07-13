n = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))

mx, mn = -1e9, 1e9

def solve(index, res, add, sub, mul, div):
    global mx, mn

    if index >= n:
        mx = max(mx, res)
        mn = min(mn, res)
        return

    if add > 0:
        solve(index + 1, res + nums[index], add - 1, sub, mul, div)
    if sub > 0:
        solve(index + 1, res - nums[index], add, sub - 1, mul, div)
    if mul > 0:
        solve(index + 1, res * nums[index], add, sub, mul - 1, div)
    if div > 0:
        solve(index + 1, res // nums[index] if res > 0 else -((-res)//nums[index]), add, sub, mul, div - 1)

solve(1, nums[0], operation[0], operation[1], operation[2], operation[3])
print(mx)
print(mn)