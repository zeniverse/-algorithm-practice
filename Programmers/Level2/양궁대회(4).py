

from copy import deepcopy


n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

candidate = []
diff = 0

def compare(origin, new):
    for i in range(10, -1, -1):
        if origin[i] > new[i]:
            return False
        elif origin[i] < new[i]:
            return True

def dfs(n, score, info, ryan):
    global candidate, diff
    if n == 0 or score == 0:
        if score == 0:
            ryan[10] = n

        total_a, total_r = 0, 0

        for i in range(11):
            if info[i] == 0 and ryan[i] == 0:
                continue

            if info[i] >= ryan[i]:
                total_a += (10 - i)
            else:
                total_r += (10 - i)

        if total_r > total_a:
            if diff < (total_r - total_a):
                diff = total_r - total_a
                candidate = deepcopy(ryan)
            elif diff == (total_r - total_a) and compare(candidate, ryan):
                candidate = deepcopy(ryan)
        return

    
    idx = 10 - score
    # ryan이 화살을 쏘는 경우
    if n > info[idx]:
        tmp = deepcopy(ryan)
        tmp[idx] = info[idx] + 1

        dfs(n - info[idx] - 1, score - 1, info, tmp)

    # ryan이 화살을 포기하는 경우
    tmp = deepcopy(ryan)
    dfs(n, score - 1, info, tmp)

def solution(n, info):
    global candidate
    ryan = [0 for _ in range(11)]
    dfs(n, 10, info, ryan)

    return candidate if candidate else [-1]

print(solution(n, info))



