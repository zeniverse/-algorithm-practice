s = ")()("

def solution(s):
    x = 0

    for i in s:
        if x < 0:
            break
        
        # 삼항 연산자 중첩으로 사용
        # [True1] if [Condition1] else [True2] if [Condition2] else [False]
        x = x + 1 if i == '(' else x - 1 if i == ')' else x

    return x == 0

print(solution(s))


