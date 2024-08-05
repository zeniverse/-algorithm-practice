from itertools import combinations

def solution(places):
    answer = []

    def check(case):
        for c in case:
            x1, y1 = c[0]
            x2, y2 = c[1]
            dist = abs(x1-x2) + abs(y1-y2)

            if dist <= 2:
                if x1 == x2:
                    if arr[x1][max(y1, y2) - 1] != 'X':
                        return False
                elif y1 == y2:
                    if arr[max(x1, x2) - 1][y1] != 'X':
                        return False
                else:
                    if arr[x1][y2] != 'X' or arr[x2][y1] != 'X':
                        return False
        return True

    for p in places:
        arr = []
        for i in p:
            arr.append(list(i))

        spot = []
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 'P':
                    spot.append([i, j])

        case = list(combinations(spot, 2))

        if check(case):
            answer.append(1)
        else:
            answer.append(0)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))