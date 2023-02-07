

n = 8
a = 4
b = 7

def solution(n, a, b):

    count = 0

    while a != b:
        count += 1

        a = (a + 1)//2
        b = (b + 1)//2

        # a값과 b값에 +1을 한 후 2로 나누면
        # 다음 라운드에서의 번호를 구할 수 있다
        # ex) a = (5//2), b = (8//2) -> 두번째 라운드의 순서가 됨

        
    return count

print(solution(n, a, b))

