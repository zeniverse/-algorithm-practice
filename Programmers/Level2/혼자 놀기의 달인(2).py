
cards = [8,6,3,7,2,5,1,4]

def solution(cards):
    visited = [False] * len(cards)
    group = []

    for i in range(len(cards)):
        cnt = 0
        while not visited[i]:
            visited[i] = True
            i = cards[i] - 1
            cnt += 1
        group.append(cnt)

    group.sort(reverse=True)

    return group[0] * group[1]

print(solution(cards))