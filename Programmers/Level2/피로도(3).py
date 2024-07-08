from itertools import permutations

dungeons = [[80,20],[50,40],[30,10]]
k = 80

def solution(k, dungeons):
    answer = 0

    for per in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0

        for need, spend in per:
            if tmp >= need:
                tmp -= spend
                cnt += 1

        answer = max(cnt, answer)

    return answer

print(solution(k, dungeons))