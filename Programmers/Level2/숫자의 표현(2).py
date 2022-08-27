
n = 15

def solution(n):
    res = 0

    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j

            if sum == n:
                res += 1
                break
            elif sum > n:
                break

    return res

print(solution(n))