number, limit, power = 10, 3, 2

def getDivisor(n):
    arr = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.add(i)
            arr.add(n // i)

    return len(arr)

def solution(number, limit, power):
    res = 0

    for i in range(1, number + 1):
        count = getDivisor(i)

        if count > limit:
            res += power
        else:
            res += count

    return res

print(solution(number, limit, power))