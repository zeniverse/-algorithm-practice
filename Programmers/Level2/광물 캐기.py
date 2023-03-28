from collections import deque

def solution(picks, minerals):
    res = 0
    tiredList = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    dic = {
        "diamond":0,
        "iron" : 1,
        "stone" : 2
    }
    info = []

    minerals = minerals[:5 * sum(picks)]
    queue = deque(minerals)

    while queue:
        cnt = 0
        useDia, useIron, useStone = 0, 0, 0

        while cnt < 5:
            cnt += 1
            mineral = queue.popleft()

            useDia += tiredList[0][dic[mineral]]
            useIron += tiredList[1][dic[mineral]]
            useStone += tiredList[2][dic[mineral]]

            if not queue:
                break

        info.append([useDia, useIron, useStone])
    info.sort(key = lambda x: [x[2], x[1], x[0]])


    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                res += info.pop()[idx]
            else:
                return res
    return res

# 다이아, 철, 돌
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))