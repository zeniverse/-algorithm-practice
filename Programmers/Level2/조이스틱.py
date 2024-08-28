name = "JAN"

res = 0

min_move = len(name) - 1

for i, char in enumerate(name):
    res += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    next = i + 1
    while next < len(name) and name[next] == 'A':
        next += 1

    # i * 2 + len(name) - next : 현재 i 까지 이동한 커서에서 다시 원점으로 돌아간다 (i * 2)
    # 이어서 왼쪽으로 A가 아닌 다른 알파벳이 시작되는 가장 왼쪽 알파벳 위치를 찾는다 
    # 즉 i에서 왼쪽으로만 이동함 == 연속된 A의 왼쪽에서 시작

    # i + 2 * (len(name) - next) : 현재 i에서 연속된 A를 지나 가장 오른쪽 끝가지 이동한다
    # 그리고 다시 왼쪽으로 이동해 A가 아닌 다른 알파벳을 만날때까지 이동한다
    # 즉 i에서 연속된 A를 넘어 오른쪽으로 이동 == 연속된 A의 오른쪽에서 시작

    # https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
    min_move = min(min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next))


res += min_move
print(res)





