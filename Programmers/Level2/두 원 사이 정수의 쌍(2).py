
def solution(r1, r2):
    res = 0

    y_min, y_max = r1, r2

    for x in range(0, r2):
        # max를 줄여서 범위 줄이기
        while r2 ** 2 < y_max**2 + x**2:
            y_max -= 1

        # min을 줄여서 범위 줄이기
        # 1사분면만 체크할 예정이기 때문에 min 값이 0이 되면 안된다(중복문제)
        while y_min - 1 and r1 ** 2 <= (y_min - 1) ** 2 + x ** 2:
            y_min -= 1

        res += y_max -y_min + 1
    
    return res * 4

r1, r2 = 2, 3
print(solution(r1, r2))