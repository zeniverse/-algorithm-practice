
n = 10

def solution(n):
    arr = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in arr:
            arr -= set(range(2 * i, n + 1, i))

    return len(arr)

print(solution(n))

