

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            elif ryan[i] > info[i]:
                s += (10 - i)
            else:
                s -= (10 - i)
        return s

    def dfs(idx, left, ryan):
        global answer, result

        if idx == -1 and left == 1:
            return
        
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx - 1, left - i, ryan)
            ryan[idx] = 0

    answer = [0] * 11
    result = 0
    dfs(10, n, [0 for _ in range(11)])

print(solution(n, info))



