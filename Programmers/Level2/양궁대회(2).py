
from itertools import combinations_with_replacement

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

def solution(n, info):

    res = [-1]
    maxDiff = -1

    # combinations_with_replacement를 통해 0~10까지의 숫자를 n개 만큼 출력할 수 있는 모든 경우의 수를 구한다
    for combi in combinations_with_replacement(range(11), n):
        # print(list(combi))

        info2 = [0] * 11

        # 10 - combi에 담긴 값을 진행해, 라이언이 쏠 수있는 모든 경우의 수를 info2에 담아준다.
        for i in combi:
            info2[10 - i] += 1

        # print('**', info2)

        apeach, ryan = 0, 0

        for idx in range(11):
            if info[idx] == info2[idx] == 0:
                continue
            elif info[idx] >= info2[idx]:
                apeach += (10 - idx)
            else:
                ryan += (10 - idx)


        if apeach < ryan:
            diff = ryan - apeach

            # 점수가 낮은 화살을 쏜 경우부터 확인하기 때문에
            # maxDiff가 같은 경우라도 info2를 출력하면, 낮은 점수가 많은 결과가 출력된다.
            if maxDiff < diff:
                maxDiff = diff
                res = info2

    return res


print(solution(n, info))