
from collections import deque

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

def bfs(n, info):
    ans = []
    queue = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxDiff = 0

    while queue:
        current, arrow = queue.popleft()

        if sum(arrow) == n:
            apeach, ryan = 0, 0

            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += (10 - i)
                    else:
                        ryan += (10 - i)

            if apeach < ryan:
                diff = ryan - apeach

                if maxDiff > diff:
                    continue

                if maxDiff < diff:
                    maxDiff = diff
                    ans.clear()

                ans.append(arrow)

        elif sum(arrow) > n:
            continue

        # 마지막으로 과녁을 쏠 차례일때, 화실의 개수(n)이 남는 경우
        # 마지막 0점에 화살을 다 사용해준다
        elif current == 10:
            tmp = arrow.copy()
            tmp[current] = n - sum(tmp)
            queue.append((-1, tmp))

        # 라이언의 현재 점수를 어피치보다 높은 점수로 만들어 점수를 얻어가는 경우
        # 라이언의 점수를 0점으로 만들어, 어피치가 점수를 얻어가는 경우
        # 두 가지 경우로 나눠서 queue에 값을 추가해준다.
        else:
            tmp = arrow.copy()
            tmp[current] = info[current] + 1
            queue.append((current + 1, tmp))

            tmp2 = arrow.copy()
            tmp2[current] = 0
            queue.append((current + 1, tmp2))

    return ans



def solution(n, info):
    results = bfs(n, info)

    if not results:
        return [-1]
    if len(results) == 1:
        return results[0]
    else:
        # 높은 점수부터 화살을 쏘도록 구현했기 때문에 가장 마지막 값을 return하면,
        # 낮은 점수를 많이 맞춘 결과가 된다(조건)
        return results[-1]

print(solution(n, info))