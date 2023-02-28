

def solution(stones, k):
    left = 1
    right = max(stones)
    res = 0

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for i in stones:
            if i - mid <= 0:
                count += 1
            else:
                count = 0

            if count >= k:
                break

        if count >= k:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))