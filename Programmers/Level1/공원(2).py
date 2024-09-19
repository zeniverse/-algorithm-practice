def solution(mats, park):
    answer = -1
    n, m= len(park), len(park[0])
    mats.sort()

    for w in mats:
        for i in range(n):
            for j in range(m):
                if not park[i][j].isalpha():
                    count = 0
                    for r in range(i, min(n, i + w)):
                        for c in range(j, min(m, j + w)):
                            if not park[r][c].isalpha():
                                count += 1
                    
                    if count == w * w:
                        answer = w
    return answer

wallet, bill = [5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

print(solution(wallet, bill))

