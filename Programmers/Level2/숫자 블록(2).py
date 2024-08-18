
begin = 1
end = 10

def maxdivisor(num):
    if num == 1:
        return 0
    res = [1]

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i <= 1e7:
            res.append(i)
            if num // i <= 1e7 and num // i != num:
                res.append(num//i)
    return max(res)


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(maxdivisor(i))
    return answer

print(solution(begin, end))
