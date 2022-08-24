

def solution(n):
    res = [0] * (n + 1)

    res[0] = 0
    res[1] = 1

    for i in range(2, n + 1):
        res[i] = ((res[i - 1] % 1234567) + (res[i - 2] % 1234567)) % 1234567
        # res[i] = (res[i - 1]+ res[i - 2]) % 1234567

    print(res)

    return res[n]

print(solution(5))