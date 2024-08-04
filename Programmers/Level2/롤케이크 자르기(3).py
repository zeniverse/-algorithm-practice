
topping = [1, 2, 1, 3, 1, 4, 1, 2]

def solution(topping):
    answer = 0

    l, r = 0, len(topping)
    idx1 = 0

    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))

        if left < right:
            l = m + 1
        else:
            idx1 = m
            r = m - 1

    l, r = 0, len(topping)
    idx2 = 0

    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))

        if left <= right:
            idx2 = m
            l = m + 1
        else:
            r = m - 1
    return max(idx2 - idx1 + 1, 0)

print(solution(topping))