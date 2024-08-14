

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

def solution(n, info):

    answer = [0 for _ in range(11)]
    tmp = [0 for _ in range(11)]
    maxDiff = 0

    for subset in range(1, 1 << 10):
        # 비트로 표현한다 생각해서 10 자리를 둔 이진수를 만든다고 생각한다
        # ex) 0000001010, 0000000001 이런식으로
        # 그래서 1 ~ 2의 10승까지 범위를 subset으로 칭한다
        ryan = 0
        apeach = 0
        cnt = 0

        for i in range(10):
            if subset & (1 << i):
                # 비트 연산자를 통해 계산
                # subset에서 i번째 자리가 1이라면 참
                ryan += (10 - i)
                # 라이언이 쏘아야 하는 화살의 갯수는 어피치가 쏜 화살의 갯수보다 1개 많아야한다
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    # 어피치가 0개가 아니라면
                    apeach += (10 - i)

        if cnt > n: continue

        # 어피치보다 +1씩 해서 더 많이 쏴서 점수를 많이 얻도록 만들었지만
        # 아직 화살의 갯수가 남았다면, 0점에 나머지 화살을 다 쏜다
        tmp[10] = n - cnt

        # maxDiff가 같은 경우 점수가 낮은 화살이 더 많은지 확인
        if ryan - apeach == maxDiff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    maxDiff = ryan - apeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break

        elif ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = tmp[:]

    if maxDiff == 0:
        answer = [-1]
    
    return answer

print(solution(n, info))



