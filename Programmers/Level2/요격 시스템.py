
targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

def solution(targets):
    answer = 0

    shoot = -1
    targets.sort(key=lambda x:[x[1], x[0]])

    for target in targets:
        if target[0] >= shoot:
            answer += 1
            shoot = target[1]

    return answer

print(solution(targets))