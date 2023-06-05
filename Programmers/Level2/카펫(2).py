
def solution(brown, yellow):
    total = brown + yellow

    for i in range(3, int(total ** 0.5) + 1):
        if total % i == 0:
            m = total // i

            if (i - 2) * (m - 2) == yellow:
                return [m, i]
            
brown = 10
yellow = 2
print(solution(brown, yellow))
