import copy


n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

maxDiff = 0
res = []

def claculator(arr1, arr2):
    enemy, my = 0, 0

    for i in range(11):
        if (arr1[i], arr2[i]) == (0, 0):
            continue
        if arr1[i] >= arr2[i]:
            enemy += (10 - i)
        else:
            my += (10 -i)

    return my - enemy



def dfs(info, ryan, n, i):
    global maxDiff, res

    if i == 11:
        # 아직 화살이 남은 경우, 마지막 0 점에 남은 화살을 다 쏴준다
        if n != 0:
            ryan[10] = n
        
        diff = claculator(info, ryan)

        if diff <= 0:
            return

        arrow = copy.deepcopy(ryan)

        if diff > maxDiff:
            maxDiff = diff
            res = [arrow]
            return

        if diff == maxDiff:
            res.append(arrow)
        
        return 

    
    #점수를 얻는 경우
    if info[i] < n:
        ryan.append(info[i] + 1)
        dfs(info, ryan, n - (info[i] + 1), i + 1)
        ryan.pop()

    # 점수를 얻지 않는 경우(0점)
    ryan.append(0)
    dfs(info, ryan, n, i + 1)
    ryan.pop()



def solution(n, info):
    global maxDiff, res

    dfs(info, [], n, 0)

    if not res:
        return [-1]
    
    res.sort(key=lambda x: x[::-1], reverse=True)
    return res[0]


print(solution(n, info))