

def solve(total, idx):
    global mx, mn

    if idx == (n - 1):
        mx = max(mx, total)
        mn = min(mn, total)
        return
    
    for i in range(4):
        if operation[i] != 0:
            operation[i] -= 1

            if i == 0:
                solve(total + nums[idx + 1], idx + 1)
            elif i == 1:
                solve(total - nums[idx + 1], idx + 1)
            elif i == 2:
                solve(total * nums[idx + 1], idx + 1)
            else:
                solve(int(total/nums[idx + 1]), idx + 1)

            operation[i] += 1

n = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))
mx, mn = -1e9, 1e9

solve(nums[0], 0)
print(mx)
print(mn)