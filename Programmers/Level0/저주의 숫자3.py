
n = 40

def solution(n):
    res = 0
    for i in range(n):
        res += 1

        while True:
            if res % 3 == 0 or '3' in str(res):
                res += 1
            else:
                break

    return res
    

print(solution(n))