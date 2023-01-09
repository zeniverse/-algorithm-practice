
msg = 'KAKAO'

def solution(msg):
    res = []
    # 알파벳 순서대로 넣기
    alpha = {chr(e + 64):e for e in range(1, 27)}

    while True:
        if msg in alpha:
            res.append(alpha[msg])
            break
        
        for i in range(1, len(msg) + 1):
            # 현재길이 까지의 문자가 alpha에 없다면,
            # 현재길이 -1 까지의 문자의 숫자를 res에 추가해준다.
            # 현재 길이 까지의 문자는 alpha에 추가
            if msg[0:i] not in alpha:
                res.append(alpha[msg[0:i - 1]])
                alpha[msg[0:i]] = len(alpha) + 1
                msg = msg[i - 1:]
                break

    return res

print(solution(msg))