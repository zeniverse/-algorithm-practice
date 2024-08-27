
m, n = 10, 10
startX, startY = 3, 7
balls = [[7, 7], [2, 7], [7, 3]]

def solution(m, n, startX, startY, balls):
    answer = []

    for i in balls:
        x, y = i[0], i[1]
        

        # 사방의 벽으로 부딪혔을 경우를 모두 계산해 작은 값을 계산해주려고 한다
        # 단, 값을 계산하기 위해서는 대칭되는 점을 찾아서 출발점에서~대칭되는 점의 일자 길이를 구해주면 된다.
        # 그러니까 아래 블로그를 보면 
        # https://silverstonec.tistory.com/56
        # y축을 기준으로 대칭되는 A'를 찾아 최소 길이를 찾는것과 같다
        # 대신 이 문제에선 y축 기준으로 대칭이 아니라, 사방의 벽 기준으로 대칭되는 것

        # 점(x, y)와 점(a, b)사이의 거리는
        # 루트((a - x) ** 2 + (b - y) ** 2)

        # 위쪽 벽을 통과한 반사
        # (startX, startY)에서 (x, n + (n - y)) 까지의 거리
        # y 좌표가 저렇게 된 이유: 예를들어 기존 공의 위치가 (6, 8) 이고 n이 10일때
        # 기존 공의 위치에서 위쪽 전장까지의 길이는 n - y = d다
        # 여기다가 대칭 선을 기준으로 n + d만큼 떨어져 있다
        # (우선 n밖으로 대칭된 점이기 때문에 n에다가 + 떨어진 만큼 더해주는 것)
        # 즉, n + n - y == 2n - y
        a = (startX - x) ** 2 + (startY - (y + (n-y) * 2)) ** 2
        
        # 왼족 벽을 통과한 반사
        # (startX, startY) (-x, y)
        b = (startX + x) ** 2  + (startY - y) ** 2

        # 아랫쪽 벽을 통과한 반사
        # (startX, startY) (x, -y)
        c = (startX - x) ** 2 + (startY + y) ** 2

        # d 오른쪽 벽을 통과한 반사
        # (startX, startY) (2m - x, y)
        # 위쪽으로 반사할때와 똑같이 반사된 위치의 점은 m - x 만큼 이동 + m 만큼 추가로 이동
        d = (startX - (2*m - x)) ** 2 + (startY - y) ** 2

        # 예를 들어, 공이 바로 직선상에 위치해 있을 때, 반사된 경로가 실제로 더 먼 거리를 유발할 수 있기 때문에
        # 이러한 경우는 아주 큰 값(예: m**2 + n**2)으로 설정하여 해당 경로가 선택되지 않도록 합니다.
        if startY == y and x < startX:
            b = m ** 2 + n ** 2
        if startX == x and y < startY:
            c = m ** 2 + n ** 2
        if startY == y and x > startX:
            d = m ** 2 + n ** 2
        if startX == x and y > startY:
            a = m ** 2 + n ** 2

        answer.append(min(a, b, c, d))
    return answer



print(solution(m, n, startX, startY, balls))