
# 진법, 미리 구할 숫자의 갯수, 게임에 참가하는 인원, 튜브 순서
n, t, m, p = 16, 16, 2, 1

def solution(n, t, m, p):
    digit = '0123456789ABCDEF'
    answer = '0'

    for num in range(1, t * m):
        tmp = ""
        while num > 0:
            tmp = digit[num % n] + tmp
            num //= n
        answer += tmp
    
    return answer[p -1:t*m:m]

print(solution(n, t, m, p))