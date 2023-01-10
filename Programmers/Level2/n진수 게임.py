import string

# 진법, 미리 구할 숫자의 갯수, 게임에 참가하는 인원, 튜브 순서
n, t, m, p = 16, 16, 2, 1

# 진법 변환
tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    res = ''
    num = ''

    for i in range(0, t * m + 1):
        num += convert(i, n)
    
    return ''.join(num[p-1::m][:t])

print(solution(n, t, m, p))