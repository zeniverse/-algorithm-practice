
def solution(n):
    res = 0
    nums = [i for i in range(1, n + 1)]

    interval_sum = 0
    end = 0

    for start in range(n):
        while interval_sum < n and end < n:
            interval_sum += nums[end]
            end += 1

        if interval_sum == n:
            res += 1
        
        interval_sum -= nums[start]

    return res

print(solution(15))