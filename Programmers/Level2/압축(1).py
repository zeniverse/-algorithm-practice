
msg = 'TOBEORNOTTOBEORTOBEORNOT'

def solution(msg):
    res = []

    # 리스트에 알파벳 순서대로 넣기
    alpha = []

    for i in range(65, 91):
        alpha.append(chr(i))


    # 문자별로 위치 찾기

    s = msg[0]
    i = 0

    while i != len(msg):
        if s in alpha:
            if i != len(msg) - 1:
                i += 1
            else:
                res.append(alpha.index(s) + 1)
                break
            s += msg[i]

        else:
            alpha.append(s)
            res.append(alpha.index(s[:-1]) + 1)
            s = msg[i]

    return res

print(solution(msg))