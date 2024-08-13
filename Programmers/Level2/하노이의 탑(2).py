
def solution(n):
    def hanoi(n, start, end, help):
        if n == 1:
            yield [start, end]
        else:
            yield from hanoi(n - 1, start, help, end)
            yield [start, end]
            yield from hanoi(n - 1, help, end, start)

    return list(hanoi(n, 1, 3, 2))

n = 2
print(solution(n))

# 'yield'는 함수의 실행을 일시 중지하고 호출자에게 값을 반환한 후, 함수의 실행을 재개한다.
# 이를 통해 함수는 이전 상태를 기억하고 다음 호출 때 이어서 실행할 수 있다.
# 'yield'는 주로 반복 가능한 객체를 생성하는 데 사용

# return은 값을 반환하고 함수의 실행을 종료한다.
# yield는 값을 반환하고 함수의 실행을 일시 중지한 후 재개한다.
# yield는 주로 반복 가능한 객체, 즉 제너레이터를 생성하는 데 사용된다.