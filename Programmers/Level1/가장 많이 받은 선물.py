friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]


def solution(friends, gifts):
    gr = {}

    for i in friends:
        gr[i] = [0, {}]

        for j in friends:
            if i != j:
                gr[i][1][j] = 0

    for i in gifts:
        a, b = i.split()

        gr[a][0] += 1
        gr[a][1][b] += 1
        gr[b][0] -= 1
        gr[b][1][a] -= 1

    print(gr)
    res = [0] * len(friends)

    for a, values in gr.items():
        idx = friends.index(a)
        ans = values[0]

        for b, count in values[1].items():
            if count > 0:
                res[idx] += 1
            elif count == 0:
                if ans > gr[b][0]:
                    res[idx] += 1

    return max(res)

print(solution(friends, gifts))
    