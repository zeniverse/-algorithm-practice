N = 4
stages = [1,2,3,2,1]

def solution(N, stages):
    answer = [0] * N
    player = len(stages)

    for i in range(N):
        try:
            answer[i] = [i + 1, stages.count(i + 1) / player]
        except:
            answer[i] = [i + 1, 0]
        
        player -= stages.count(i + 1)

    return [i[0] for i in sorted(answer, key=lambda x: x[1], reverse=True)]


print(solution(N, stages))
