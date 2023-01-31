
def solution(n, l, r):
    res = r - l + 1

    for num in range(l - 1, r):
        while num >= 1:
            a, b = divmod(num, 5)
            # print(a, b)

            if b == 2 or a == 2:
                res -= 1
                break
            num = a

    return res

n, l, r = 2, 4, 17
print(solution(n, l, r))